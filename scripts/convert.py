#!/usr/bin/env python
# encoding: utf-8

import json
from sys import argv
from os import system
from os import remove
from os.path import exists


def get_json(fname):
    with open(fname) as fd:
        for line in fd.readlines():
            if not line.startswith('raw:'):
                continue
            line = line.replace('raw: ', '')
            line = line.rstrip()
            line = line.lstrip()

            data = json.loads(line)
    return data


def get_datetime_dict(datetime):
    date, time, tmz = datetime.split(' ')
    year, month, day = date.split('-')
    hour, minu, sec = time.split(':')
    return {
        'YYYY': year,
        'YY': year[2:],
        'MM': month,
        'DD': day,
        'hh': hour,
        'mm': minu,
        }


def exit_error(msg):
    print msg
    exit(1)

if __name__ == '__main__':
    if len(argv) != 2:
        exit_error(u'Utilização: {} fname.md'.format(argv[0]))

    fname = argv[1]
    if not fname.endswith('.md'):
        exit_error(u'Por favor, indique um arquivo em markdown.')

    if not exists(fname):
        exit_error(u'Arquivo {} informado não existe.'.format(fname))

    data = get_json(fname)

    slug = unicode(data['slug']).encode('utf-8')
    try:
        title = unicode(data['title']).encode('utf-8')
    except KeyError:
        title = ' '.join(
            [word.capitalize() for word in slug.split('-')]
            )

    if data['type'] == 'photo':
        body = []
        for i in data['photos']:
            body.append(
                '<img src="{}"/>\n'.format(i['original_size']['url'])
                )
        body = ''.join([part for part in body])
        body += unicode(data['caption']).encode('utf-8')

    elif data['type'] == 'text':
        body = unicode(data['body']).encode('utf-8')

    elif data['type'] == 'quote':
        body = ''
        if 'text' in data:
            body += '<p>{}</p>'.format(
                unicode(data['text']).encode('utf-8')
                ) + '\n'
        if 'source' in data:
            body += unicode(data['source']).encode('utf-8')

    elif data['type'] == 'video':
        body = ''
        if 'caption' in data:
            body += unicode(data['caption']).encode('utf-8') + '\n'
        if 'player' in data:
            body += data['player'][-1]['embed_code']

    elif data['type'] == 'link':
        body = ''
        if 'description' in data:
            body += unicode(data['description']).encode('utf-8') + '\n'

    else:
        print 'tipo desconhecido: {}'.format({data['type']})
        body = ''
        exit(1)

    outfile_rst = unicode("{}.rst".format(slug)).encode('utf-8')
    outfile_html = unicode("{}.html".format(slug)).encode('utf-8')
    datetime = get_datetime_dict(data['date'])
    try:
        tags = u', '.join(data['tags'])
        tags = tags.encode('utf-8')
    except KeyError:
        tags = ''

    with open(outfile_html, 'w') as fd:
        fd.write(body)

    with open(outfile_rst, 'w') as fd:
        fd.write('{}\n'.format(title))
        fd.write('#'*len(title)+'\n')
        fd.write(':slug: {}\n'.format(slug))
        fd.write(
            ':date: {YYYY}-{MM}-{DD} {hh}:{mm}\n'.format(**datetime)
            )
        fd.write(':category:\n')
        fd.write(':tags: {}\n\n'.format(tags))

    system(
        'pandoc -i {} -f html -t rst >> {}'.format(outfile_html, outfile_rst)
        )
    remove(outfile_html)
    system("touch -t {YY}{MM}{DD}{hh}{mm} {outfile_rst}".format(
        outfile_rst=outfile_rst, **datetime
        ))
