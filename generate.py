#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=['jinja_markdown.MarkdownExtension']
)
indexTemplate = env.get_template('index.html')
bomTemplate = env.get_template('bom.html')

with open('index.md', 'r') as stream:
    index = stream.read()

with open("a4000-rb-bom.yml", 'r') as stream:
    raw = list(yaml.safe_load_all(stream))
    data = {
        'version': raw[0]['version'],
        'date': raw[0]['date'],
        'bom': raw[1],
        'index': index,
    }

with open('docs/index.html', 'w') as out:
    out.write(indexTemplate.render(data))

with open('docs/a4000-bom.html', 'w') as out:
    out.write(bomTemplate.render(data))
