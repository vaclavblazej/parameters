#!/usr/bin/env python3

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
                     filename='my-diagram',
                     node_attr={'color': 'lightblue2', 'style': 'filled'})

u.attr(size='6,6')

nos_path = os.path.expanduser('~') + '/Dropbox/Projects/noosphere'
sys.path.insert(1, nos_path)
from noosphere import Noosphere
from noosphere.data import FileDB

nos = Noosphere(FileDB("par.json"))


def check_type(x, tp):
    if 'type' not in x:
        return False
    return x['type']['!id'] == tp


def check_is_par(x):
    return check_type(x, '!TrvG50')


def check_is_connection(x):
    return check_type(x, '!jgWdIT')


nodes = {}
entries = list(filter(check_is_par, nos.data.all()))
connections = list(filter(check_is_connection, nos.data.all()))
for entry in entries:
    col = avg_color('e0e0e0', '90c0f0', entry['importance'])
    u.node(entry['!id'], label=entry['name'], shape='box', color='#'+col)
for connection in connections:
    u.edge(connection['from']['!id'], connection['to']['!id'])

u.view()
