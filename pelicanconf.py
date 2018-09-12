#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carson Zhang'
SITENAME = "Carson's Blog"
SITEURL = 'http://zmcddn.github.io'

PATH = 'content'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/zmcddn'),
          ('Kaggle', 'https://www.kaggle.com/zmcddn'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Jupytor Notebook Settings
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = [ './plugins' ]
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']

# Theme Setting
THEME = "theme/pelican-themes/tuxlite_tbs"