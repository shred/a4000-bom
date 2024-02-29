#!/usr/bin/env python3

import re
import xlsxwriter
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
                print('    components: ["{}"]'.format('", "'.join(expected)))
                raise ValueError('Part "{}": Incorrect component order'.format(reference))

def xlsxExport(data):
    workbook = xlsxwriter.Workbook('docs/a4000-bom.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.freeze_panes(1, 0)
    fmtTitle = workbook.add_format({'bold': True, 'bg_color': '#f47176'})
    fmtSection = workbook.add_format({'bold': True, 'bg_color': '#e6e6e6'})
    fmtFooter = workbook.add_format({'bg_color': '#83a9d8', 'valign': 'vcenter', 'indent': 2})
    fmtComponents = workbook.add_format({'text_wrap': True})
    fmtBold = workbook.add_format({'bold': True})

    row = 0
    titles = ['Part Id', 'Qty', 'Part', 'Remark', 'Package', 'Mouser', 'Components']
    widths = [      10 ,    5 ,    50 ,      50 ,       10 ,      25 ,          60 ]
    for c in range(0, len(titles)):
        worksheet.set_column(c, c, widths[c])
        worksheet.write(row, c, titles[c], fmtTitle)

    for (title, sect) in data['bom'].items():
        row += 1
        worksheet.merge_range(row, 0, row, 6, title, fmtSection)
        for item in sect:
            row += 1
            if 'id' in item:
                worksheet.write(row, 0, item['id'])
            worksheet.write(row, 1, item['quantity'])
            worksheet.write(row, 2, item['part'])
            if 'remark' in item:
                worksheet.write(row, 3, item['remark'])
            if 'package' in item:
                worksheet.write(row, 4, item['package'])
            if 'mouser' in item:
                mid = item['mouser']['id']
                mlink = 'https://www.mouser.com/ProductDetail/{}'.format(mid)
                worksheet.write_url(row, 5, mlink, string=mid)
            if 'components' in item:
                worksheet.write(row, 6, ' '.join(item['components']), fmtComponents)

    footer = [
        fmtBold, '{} Bill of Material – '.format(data['project']), 'Version: {} ({})\n'.format(data['version'], data['date']),
        'Source and latest version at {}: '.format(data['source']['repo']), '{}\n'.format(data['source']['url']),
        'License: ', '{}\n'.format(data['license']['type']),
        fmtBold, 'This content is provided "as is" and without warranties of any kind either expressed or implied.'
    ]
    row += 2
    worksheet.set_row(row, 60)
    worksheet.merge_range(row, 0, row, 6, '')
    worksheet.write_rich_string(row, 0, *footer, fmtFooter)

    workbook.close()



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
    data = dict(raw[0])
    data['bom'] = raw[1]
    data['content'] = content

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

with open('docs/diffs.html', 'w') as out:
    template = env.get_template('diffs.html')
    out.write(template.render(data))

with open('docs/other.html', 'w') as out:
    template = env.get_template('other.html')
    out.write(template.render(data))

xlsxExport(data)
