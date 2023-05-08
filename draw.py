#!/usr/bin/env python3

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
                     filename='my-diagram',
                     node_attr={'color': 'lightblue2', 'style': 'filled'})

u.attr(size='6,6')

sys.path.insert(1, '/home/blazeva1/Dropbox/Projects/noosphere')
import noosphere
import noosphere.data

database = noosphere.data.FileDB("par.json")
nos = noosphere.Noosphere(database)


def check_is_par(x):
    if 'type' not in x:
        return False
    return x['type']['!id'] == '!TrvG50'


nodes = {}
entries = list(filter(check_is_par, nos.data.all()))
for entry in entries:
    col = avg_color('e0e0e0', '90c0f0', entry['importance'])
    u.node(entry['!id'], label=entry['name'], shape='box', color='#'+col)
for entry in entries:
    if 'upper_bounds' not in entry:
        continue
    uppers = entry['upper_bounds']
    for upper in uppers:
        u.edge(entry['!id'], upper['!id'])

u.view()
