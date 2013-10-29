__author__ = 'yuetingqian'
#-*- coding: utf-8 -*-
import sys
import web
from web.contrib.template import render_mako
sys.path.append('../dao')
from dao.db import getConnection

hiapi_db = getConnection()

render = render_mako(
                    directories = ['templates'],
                    input_encoding='utf8',
                    output_encoding='utf8',
                    )
web.debug(12233)
web.config.debug = True
