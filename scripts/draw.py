#!/usr/bin/env python3

import data
import graphviz
import latex2markdown

import par_types
from par_types import Note, Cite, ISGCI, Parameter, GraphClass

from pybtex.database.input import bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('main.bib')


def latex_to_markdown(latext):
    return latex2markdown.LaTeX2Markdown(latext).to_markdown()


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


data = data.export()

print('processing data ...')
print("parameters:", len(data.parameters))
print("connections:", len(data.connections))


class DrawNode:

    def __init__(self, node):
        self.node = node

    def draw(self, digraph, entry_coloring_function):
        digraph.node(self.node.id,
                     label=self.node.name,
                     URL='./'+self.node.id,
                     shape='box',
                     color=entry_coloring_function(self.node))


def drawNode(node):
    if hasattr(data, 'equivalencies'):
        for eq in data.equivalencies:
            if eq.removed == node:
                return None
    return DrawNode(node)


def linkto(text, node_or_url):
    if hasattr(node_or_url, 'id'):
        return f'[{text}]({node_or_url.id})'
    else:
        return f'[{text}]({node_or_url})'


def remap(id):
    remap_eqiv = dict()
    for eq in data.equivalencies:
        remap_eqiv[eq.removed.id] = eq.persist.id
    if id in remap_eqiv.keys():
        return remap_eqiv[id]
    return id


def render_graph_classes(filename, entry_coloring_function):
    u = graphviz.Digraph('unix',
                         filename=filename,
                         directory="build",
                         node_attr={'color': 'lightblue2', 'style': 'filled'},
                         )
    u.attr(size='6,6', margin='0.04')
    drawNodes = list(filter(lambda x: x is not None, map(lambda x: drawNode(x), data.graph_classes)))
    for node in drawNodes:
        node.draw(u, entry_coloring_function)
    for inclusion in data.graph_inclusions:
        style = {
               "URL": './'+inclusion.id,
               "decorate": 'true',
               "lblstyle": "above, sloped",
               "color": "gray",
               "weight": "1",
        }
        u.edge(inclusion.subclass.id, inclusion.superclass.id, **style)
    u.render()
    #  print(f'Rendered ./build/{filename}.pdf')


def nop(x):
    return True


def render_parameters(filename, entry_coloring_function, filter_vertices=nop):
    u = graphviz.Digraph('unix',
                         filename=filename,
                         directory="build",
                         node_attr={'color': 'lightblue2', 'style': 'filled'},
                         )
    u.attr(size='6,6', margin='0.04')
    filterPars = list(filter(filter_vertices, data.parameters))
    drawNodes = list(filter(lambda x: x is not None, map(lambda x: drawNode(x), filterPars)))
    for node in drawNodes:
        node.draw(u, entry_coloring_function)
    filterParIds = list(map(lambda x: remap(x.id), filterPars))
    for connection in data.connections:
        frid = remap(connection.fr.id)
        toid = remap(connection.to.id)
        if frid not in filterParIds or toid not in filterParIds:
            continue
        style = {
               "URL": './'+connection.id,
               "decorate": 'true',
               "lblstyle": "above, sloped",
               "color": "gray",
               "weight": "1",
        }
        if connection.upper_bound != par_types.MAX_NONE:
            style.update({"color": "black"})
        if connection.upper_bound == par_types.LINEAR:
            style.update({"penwidth": "3.0", "weight": "100"})
        if connection.upper_bound == par_types.POLYNOMIAL:
            style.update({"penwidth": "1.0", "weight": "20"})
        if connection.upper_bound == par_types.EXPONENTIAL:
            style.update({"penwidth": "1.0", "weight": "4", "style": "dotted"})
        style.update({"label": '⬤'})
        if len(list(filter(lambda x: isinstance(x, Cite), connection.notes))) != 0:
            style.update({"fontcolor": 'black'})
        else:
            style.update({"fontcolor": 'gray'})
        arrowhead = []
        if connection.known_strict:
            arrowhead.append('icurve')
        else:
            arrowhead.append('normal')
        if connection.known_optimal_head:
            arrowhead.append('tee')
        if connection.known_optimal_tail:
            style.update({"arrowtail": 'tee', 'dir': 'both'})
        style.update({"arrowhead": 'none'.join(arrowhead)})
        u.edge(remap(connection.fr.id), remap(connection.to.id), **style)
    u.render()
    #  print(f'Rendered ./build/{filename}.pdf')


def get_close_parameters(parameter, steps=3):
    open = [parameter]
    next_open = []
    visited = set()
    for i in range(steps):
        while len(open) != 0:
            entry = open.pop()
            if entry not in visited and entry not in open:
                visited.add(entry)
                entry.hue = 1.0-i/steps
                next_open += entry.above + entry.below
                open += entry.equivalent_to
        open = next_open
        next_open = []
    return list(visited)


def color_by_hue(parameter):
    default = 'e0e0e0'
    if hasattr(parameter, 'hue'):
        return '#'+avg_color(default, '90c0f0', parameter.hue)
    else:
        return '#'+default


def color_by_inclusion(parameter, graphclass):
    if graphclass in parameter.bounded_for and graphclass in parameter.unbounded_for:
        print(f'WARNING: {parameter.name} is both bounded and unbounded for {graphclass.name}')
        col = '#6666dd'
    elif graphclass in parameter.bounded_for:
        col = '#00aa00'
    elif graphclass in parameter.unbounded_for:
        col = '#dd0000'
    else:
        col = '#ddaa00'
    return col


render_parameters('parameters', color_by_hue)
for par in data.parameters:
    close_pars = get_close_parameters(par)
    if par.id == 'p5skoj_dist':
        print(list(map(lambda x:x.name,close_pars)))
    render_parameters('local_'+par.id, color_by_hue, lambda x: x in close_pars)
for gc in data.graph_classes:
    render_parameters(gc.id, lambda x: color_by_inclusion(x, gc))
render_graph_classes('graphs', color_by_hue)
for par in data.parameters:
    render_graph_classes(par.id, lambda x: color_by_inclusion(par, x))


def format_note(note):
    res = ''
    if isinstance(note, ISGCI):
        gc_base = 'https://www.graphclasses.org'
        link = None
        if isinstance(note.parent, Parameter):
            link = f'{gc_base}/classes/par_{note.code}.html'
        if isinstance(note.parent, GraphClass):
            link = f'{gc_base}/classes/gc_{note.code}.html'
        if link is not None:
            res += f'* graphclasses.org: [{note.parent.name}]({link})\n'
    if isinstance(note, Note):
        res += f'* {latex_to_markdown(note.text)}\n'
    if isinstance(note, Cite):
        res += '* '
        if 'url' in note.kwargs:
            res += f'[↗]({note.kwargs["url"]}) '
        if 'source' in note.kwargs:
            source = note.kwargs["source"]
            res += f'[{source.sourcekey}](../{source.id}): '
        res += latex_to_markdown(note.kwargs['text'])
        res += '\n'
    return res


def embed_pdf(name, height):
    return f'\n<object data="{name}.pdf" type="application/pdf" width="100%" height="{height}px"><embed src="{name}.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="{name}.pdf">Download PDF</a>.</p></embed></object>\n\n'


def markdown_parameter(parameter):
    content = ''
    content += '## ' + parameter.name
    #  if parameter.abbreviation is not None:
        #  content += ' (' + parameter.abbreviation + ')'
    #  content += f' <span id={parameter.id}></span>'
    content += '\n'
    if len(parameter.notes) != 0:
        for note in parameter.notes:
            content += format_note(note)
    content += embed_pdf('../local_' + parameter.id, 480)
    content += embed_pdf('../' + parameter.id, 480)
    return content


def markdown_graph_class(graph_class):
    content = ''
    content += f'## {graph_class.name}'
    #  content += f' <span id={graph_class.id}></span>'
    content += '\n'
    for note in graph_class.notes:
        content += format_note(note)
    content += '\n'
    content += f'[Graph class PDF](../{graph_class.id}.pdf)\n'
    content += embed_pdf('../' + graph_class.id, 480)
    return content


def markdown_connection(connection):
    content = ''
    fr = connection.fr
    to = connection.to
    content += '## '
    content += f'[{fr.name}](../{fr.id})'
    content += ' → '
    content += f'[{to.name}](../{to.id})'
    #  content += f' <span id={connection.id}></span>'
    content += '\n'
    for note in connection.notes:
        content += format_note(note)
    return content


def markdown_source(source):
    content = ''
    content += f'## {source.sourcekey}'
    #  content += f' <span id={source.id}></span>'
    content += '\n'
    if source.sourcekey in bib_data.entries:
        entry = bib_data.entries[source.sourcekey]
        url = None
        fields = entry.fields
        if 'url' in fields:
            url = fields['url']
        elif 'doi' in fields:
            url = 'https://www.doi.org/' + fields['doi']
        if url is not None:
            content += f'[{url}]({url})\n'
        content += '```\n'
        content += entry.to_string('bibtex')
        content += '```\n'
        for note in source.notes:
            content += format_note(note)
        content += '\n'
    return content


def markdown_landing_page():
    content = ''
    content += '**PDF Controls:**\n'
    content += 'Zoom with Ctrl+wheel, Click nodes or edge-circles to open relevant page.\n'
    content += '\n'
    content += 'Gray edges are waiting for the proof with a link to be added to this database.'
    content += 'Edge style represents bound:'
    content += 'Thick = linear, '
    content += 'Thin = polynomial, and '
    content += 'Dashed = exponential.\n'
    content += '\n'
    content += 'This page lists:\n'
    content += '* [parameters](#parameters)\n'
    content += '* [graph classes](#graph-classes)\n'
    content += '* [sources](#sources)\n'

    content += '\n\n---\n'
    content += '# Parameters\n\n'
    content += '[Parameter hierarchy PDF](parameters.pdf)\n'
    content += embed_pdf('parameters', 480)
    content += '\n'
    content += f'{len(data.parameters)} parameters and '
    content += f'{len(data.connections)} connections\n'
    for parameter in sorted(data.parameters, key=lambda x: x.name):
        content += f'* {linkto(parameter.name, parameter)}\n'

    content += '\n\n---\n'
    content += '# Graph classes\n\n'
    content += 'Some parameters are derived from associated graph classes.\n'
    content += 'Graph classes can be also used as witnesses of proper inclusions.\n'
    content += 'For these purposes, we use the following graph class hierarchy.\n'
    content += '\n'
    content += 'We aim to have here only the graph classes that influence parameter inclusions.\n'
    content += 'Please, see [Information System on Graph Classes and their Inclusions (ISGCI)](https://www.graphclasses.org/) for an exhaustive list of graph classes and their inclusions.\n'
    content += '\n'
    content += '[Graph hierarchy PDF](graphs.pdf)\n'
    content += embed_pdf('graphs', 420)
    content += '\n'
    for graph_class in sorted(data.graph_classes, key=lambda x: x.name):
        content += f'* {linkto(graph_class.name, graph_class)}\n'

    #  for parameter in sorted(data.parameters, key=lambda x: len(x.unbounded_for) - len(x.bounded_for)):
        #  content += markdown_parameter(parameter)

    #  for graph_class in sorted(data.graph_classes, key=lambda x: len(x.has_unbounded) - len(x.has_bounded)):
        #  content += markdown_graph_class(graph_class)

    #  content += '\n\n---\n'
    #  content += '# Parameter relations\n\n'
    #  for connection in data.connections:
        #  content += f'* {linkto(connection.name, connection)}\n'
        #  content += markdown_connection(connection)

    content += '\n\n---\n'
    content += '# Sources\n\n'
    for source in data.sources:
        content += f'* {linkto(source.sourcekey, source)}\n'
        #  content += markdown_source(source)

    return content


def make_page(pagename, content):
    final_markdown = ''
    final_markdown += '---\n'
    final_markdown += 'layout: "single"\n'
    final_markdown += 'title: "Parameters hierarchy"\n'
    final_markdown += '---\n'
    final_markdown += '<!--this is a generated file-->\n\n'
    final_markdown += content
    filename = f"./build/{pagename}"
    file = open(filename, "w")
    file.write(final_markdown)
    file.close()
    #  print(f'Saved website into {filename}')


make_page("_index.md", markdown_landing_page())
for entry in data.parameters:
    make_page(f'{entry.id}.md', markdown_parameter(entry))
for entry in data.graph_classes:
    make_page(f'{entry.id}.md', markdown_graph_class(entry))
for entry in data.connections:
    make_page(f'{entry.id}.md', markdown_connection(entry))
for entry in data.sources:
    make_page(f'{entry.id}.md', markdown_source(entry))
#  for entry in data.inclusions:
    #  make_page(f'{entry.id}.md', markdown_inclusion(entry))
