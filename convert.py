#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
mdTemplate = env.get_template('bom.md')
htmlTemplate = env.get_template('bom.html')

with open("a4000-rb-bom.yml", 'r') as stream:
    raw = list(yaml.safe_load_all(stream))
    data = {
        'version': raw[0]['version'],
        'date': raw[0]['date'],
        'bom': raw[1],
    }

with open('docs/a4000-bom.md', 'w') as out:
    out.write(mdTemplate.render(data))

with open('docs/a4000-bom.html', 'w') as out:
    out.write(htmlTemplate.render(data))
