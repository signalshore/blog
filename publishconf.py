#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'https://signalshore.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
