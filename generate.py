#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader
from os import walk

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

with open('docs/index.html', 'w') as out:
    template = env.get_template('index.html')
    out.write(template.render(data))

with open('docs/a4000-bom.html', 'w') as out:
    template = env.get_template('bom.html')
    out.write(template.render(data))

with open('docs/csv.html', 'w') as out:
    template = env.get_template('csv.html')
    out.write(template.render(data))
