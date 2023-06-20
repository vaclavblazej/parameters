#!/usr/bin/env python3

#  processes the data to produce:
#  * parameters.pdf -- diagram of the parameters
#  * page.md -- website that contains the pdf and info on the parameters and bounds

import data
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


def check_type(x, tp):
    if 'type' not in x:
        return False
    return x['type']['!id'] == tp


def check_is_par(x):
    return check_type(x, '!TrvG50')


def check_is_connection(x):
    return check_type(x, '!jgWdIT')

data = data.export()
entries = data.entries
connections = data.connections

print('processing data ...')
nodes = {}
print("entries:", len(entries))
print("connections:", len(connections))
for entry in entries:
    col = avg_color('e0e0e0', '90c0f0', entry.hue)
    u.node(entry.id,
           label=entry.name,
           URL='./#'+entry.id,
           shape='box',
           color='#'+col)
for connection in connections:
    label = '◯'
    if len(connection.notes) != 0:
        label = '⬤'
    u.edge(connection.fr.id,
           connection.to.id,
           label=label,
           URL='./#'+connection.id,
           decorate='true',
           lblstyle="above, sloped")

#  u.view()
u.render()
print('Saved pdf into ./parameters.pdf')


def format_note(note):
    res = ''
    res += '* '
    if note.url is not None:
        res += f'[↗]({note.url}) '
    res += note.text
    res += '\n'
    return res


#  construct and save the website
content = ''
content += '+++\n'
content += '+++\n'
content += '<!--this is a generated file-->\n\n'
content += '**Controls:**\n'
content += 'Zoom with Ctrl+wheel and move with wheel & Shift+wheel.\n'
content += 'Click nodes or circles at edges to jump to the relevant section with definition or inclusion proof.\n'
content += 'Empty circles are waiting for the proof with a link to be added to this database.'
content += '\n'
content += '<object data="parameters.pdf" type="application/pdf" width="100%" height="480px"><embed src="parameters.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="main.pdf">Download PDF</a>.</p></embed></object>'
content += '\n\n'
content += f'entries: {len(entries)}, connections: {len(connections)}'
content += '\n\n---\n'
content += '# Parameters\n\n'
for entry in entries:
    content += '## ' + entry.name
    if entry.abbreviation is not None:
        content += ' (' + entry.abbreviation + ')'
    content += f' <span id={entry.id}></span>'
    content += '\n'
    if len(entry.notes) != 0:
        for note in entry.notes:
            content += format_note(note)
content += '\n\n---\n'
content += '# Relations\n\n'
for connection in connections:
    fr = connection.fr
    to = connection.to
    content += '## '
    content += f'[{fr.name}](#{fr.id})'
    content += ' → '
    content += f'[{to.name}](#{to.id})'
    content += f' <span id={connection.id}></span>'
    content += '\n'
    for note in connection.notes:
        content += format_note(note)

for _ in range(100):
    content += '<br>'
content += 'The space above is here just to make the relative links work nicely even for the last entries :)'
file = open("./page.md", "w")
file.write(content)
file.close()
print('Saved website into ./page.md')
