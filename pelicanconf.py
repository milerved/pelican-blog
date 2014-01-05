#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SITEURL = 'http://milerved.github.io'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

AUTHOR = u'Steven'
SITENAME = u"Steven's Blog"

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

USE_FOLDER_AS_CATEGORY = True

FILENAME_METADATA = '(?P<slug>.*)'

DEFAULT_LANG = u'zh_CN'

THEME = 'niu-x2'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images',]

# Blogroll

# Social widget
SOCIAL = (('微博', 'http://weibo.com/u/1965117033'),)

DEFAULT_PAGINATION = 10

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]

PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['extract_headings']
# extrac_headings plugin config
import md5
def my_slugify(value, sep):
    m = md5.new()
    m.update(value)
    return m.digest().encode('hex')
from markdown.extensions import headerid, codehilite
MD_EXTENSIONS = ([
    'extra',
    codehilite.CodeHiliteExtension(configs=[('linenums', False), ('guess_lang', False)]),
    headerid.HeaderIdExtension(configs=[('slugify', my_slugify)]),
    ])
MY_SLUGIFY_FUNC = my_slugify

MY_HEADING_LIST_STYLE = 'ol'
