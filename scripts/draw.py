#!/usr/bin/env python3

#  processes the data to produce:
#  * parameters.pdf -- diagram of the parameters
#  * page.md -- website that contains the pdf and info on the parameters and bounds

import os
import sys
import graphviz


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def avg_color(color1, color2, weight):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    def avg(x, y, w):
        return round((x*(1-w)) + y*w)
    new_rgb = ()
    for i in range(len(rgb1)):
        new_rgb += (avg(rgb1[i], rgb2[i], weight),)
    return rgb_to_hex(new_rgb)


u = graphviz.Digraph('unix',
                     filename='parameters',
                     node_attr={'color': 'lightblue2', 'style': 'filled'})

u.attr(size='6,6', margin='0.04')

nos_path = os.path.expanduser('~') + '/Dropbox/Projects/noosphere'
sys.path.insert(1, nos_path)
from noosphere import Noosphere
from noosphere.data import FileDB

nos = Noosphere(FileDB("../data/par.json"))


def check_type(x, tp):
    if 'type' not in x:
        return False
    return x['type']['!id'] == tp


def check_is_par(x):
    return check_type(x, '!TrvG50')


def check_is_connection(x):
    return check_type(x, '!jgWdIT')


print('processing data ...')
nodes = {}
entries = list(filter(check_is_par, nos.data.all()))
connections = list(filter(check_is_connection, nos.data.all()))
print("entries:", len(entries))
print("connections:", len(connections))
for entry in entries:
    col = avg_color('e0e0e0', '90c0f0', entry['importance'])
    u.node(entry['!id'],
           label=entry['name'],
           URL='./#'+entry['!id'],
           shape='box',
           color='#'+col)
for connection in connections:
    label = '◯'
    if 'notes' in connection:
        label = '⬤'
    u.edge(connection['from']['!id'],
           connection['to']['!id'],
           label=label,
           URL='./#'+connection['!id'],
           decorate='true',
           lblstyle="above, sloped")

for a in connections:
    for b in connections:
        for c in connections:
            if a != b and b != c and a != c:
                if a['to']['!id'] == b['from']['!id'] \
                        and b['to']['!id'] == c['from']['!id'] \
                        and c['from']['!id'] == a['from']['!id'] \
                        and c['to']['!id'] == b['to']['!id']:
                    print('transitive can be removed:', a, b, c)

#  u.view()
u.render()
print('Saved pdf into ./parameters.pdf')


def format_note(note):
    res = ''
    res += '* '
    if 'url' in note:
        res += f'[source]({note["url"]}) '
    res += note["text"]
    res += '\n'
    return res


#  construct and save the website
content = ''
content += '+++\n'
content += 'title = "Parameterized complexity hierarchy"\n'
content += '+++\n'
content += '\n\n'
content += '* Zoom with Ctrl+wheel and move with wheel & Shift+wheel\n'
content += '* Click nodes or circles at edges to jump to the relevant section with definition or inclusion proof.\n'
content += '* Any copied material has a source link -- this is the preferred way. Everything else will be slowly replaced.\n'
content += '* The sources are available [online](https://github.com/vaclavblazej/parameters), however, it is not trivial to work with.\n'
content += '\n'
content += '<object data="parameters.pdf" type="application/pdf" width="100%" height="480px"><embed src="parameters.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="main.pdf">Download PDF</a>.</p></embed></object>'
content += '\n\n'
content += '# Parameters\n\n'
for entry in entries:
    content += '## ' + entry['name']
    if 'abbreviation' in entry:
        content += ' (' + entry['abbreviation'] + ')'
    content += f' <span id={entry["!id"]}></span>'
    content += '\n'
    if 'notes' in entry:
        for note_id in entry['notes']:
            note = nos.core.call('get', note_id)
            content += format_note(note)
content += '\n\n'
content += '# Relations\n\n'
for connection in connections:
    fr = nos.core.call('get', connection['from']['!id'])
    to = nos.core.call('get', connection['to']['!id'])
    content += '## '
    content += f'[{fr["name"]}](#{fr["!id"]})'
    content += ' → '
    content += f'[{to["name"]}](#{to["!id"]})'
    content += f' <span id={connection["!id"]}></span>'
    content += '\n'
    if 'notes' in connection:
        for note_id in connection['notes']:
            note = nos.core.call('get', note_id)
            content += format_note(note)

for _ in range(100):
    content += '<br>'
content += 'The space above is here just to make the relative links work nicely even for the last entries :)'
file = open("./page.md", "w")
file.write(content)
file.close()
print('Saved website into ./page.md')
