__author__ = 'yuetingqian'
#-*- coding: utf-8 -*-
import web
from web.contrib.template import render_mako

render = render_mako(
                    directories = ['templates'],
                    input_encoding='utf8',
                    output_encoding='utf8',
                    )

web.debug(12233)
web.config.debug = True
