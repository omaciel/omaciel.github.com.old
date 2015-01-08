#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Og Maciel'
SITENAME = u'Journal of an Open Sourcee'
SITEURL = 'https://omaciel.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_USE_SUMMARY = True

# Github
GITHUB_URL = 'https://github.com/omaciel'

# Social widget
SOCIAL = (
    ('GitHub', GITHUB_URL),
    ('Twitter', 'https://twitter.com/OgMaciel'),
    ('LinkedIn', 'http://www.linkedin.com/pub/og-maciel/7/425/257/'),
    ('GoodReads', 'https://www.goodreads.com/user/show/12048315-og-maciel'),
    ('Instagram', 'http://instagram.com/ogmaciel'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [
    'extra',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

THEME = './themes/pelican-bootstrap3'
PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = [
    'summary',
    'feed_summary',
    'sitemap',
]
SUMMARY_END_MARKER = "<!-- more -->"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Disqus configuration
DISQUS_SITENAME = 'journalofanopensourcee'

# Theme serttings
BOOTSTRAP_THEME = 'united'
