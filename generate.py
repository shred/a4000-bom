#!/usr/bin/env python3

import re
import yaml
from functools import cmp_to_key
from jinja2 import Environment, FileSystemLoader
from os import walk

def compstr(s1, s2):
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

def compare(c1, c2):
    m1 = re.match(r'([A-Z]+)(\d+)([A-Z]*)', c1)
    m2 = re.match(r'([A-Z]+)(\d+)([A-Z]*)', c2)
    if m1 is not None and m2 is not None:
        pre = compstr(m1.group(1), m2.group(1))
        if pre != 0:
            return pre
        i1 = int(m1.group(2))
        i2 = int(m2.group(2))
        if i1 < i2:
            return -1
        elif i1 > i2:
            return 1
        return compstr(m1.group(3), m2.group(3))
    return compstr(c1, c2)

def validate(bom):
    for (_, sect) in bom.items():
        for item in sect:
            reference = item['id'] if 'id' in item else item['part']
            if 'components' not in item or 'quantity' not in item:
                continue
            comps = item['components']
            quantity = item['quantity']
            if len(comps) != quantity and reference not in ['390625-04', '390719-01']:
                raise ValueError('Part "{}": Quantity should be {}, but is {}'.format(reference, len(comps), quantity))
            expected = list(comps)
            expected.sort(key=cmp_to_key(compare))
            if expected != comps:
                print('    components: ["{}"]'.format(part, '", "'.join(expected)))
                raise ValueError('Part "{}": Incorrect component order'.format(reference))


env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=['jinja_markdown.MarkdownExtension']
)

content = {}
(_, _, filenames) = next(walk('content'))
for filename in filenames:
    name = filename.removesuffix('.md')
    with open('content/' + filename, 'r') as stream:
        content[name] = stream.read()

with open("a4000-rb-bom.yml", 'r') as stream:
    raw = list(yaml.safe_load_all(stream))
    data = {
        'version': raw[0]['version'],
        'date': raw[0]['date'],
        'bom': raw[1],
        'content': content,
    }

validate(data['bom'])

with open('docs/index.html', 'w') as out:
    template = env.get_template('index.html')
    out.write(template.render(data))

with open('docs/a4000-bom.html', 'w') as out:
    template = env.get_template('bom.html')
    out.write(template.render(data))

with open('docs/csv.html', 'w') as out:
    template = env.get_template('csv.html')
    out.write(template.render(data))
