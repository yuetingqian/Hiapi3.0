# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from helpers import hstring

parent = 'root'

def parser(json, outputs, parent=parent, tr=['root|properties|#int#|id'], html='', index=0):
    if isinstance(json, dict):
        for key in json:
            [html, index] = parser(json[key], outputs, parent+'|'+key, tr, html, index)
    elif isinstance(json, list):
        for item in json:
            [html, index] = parser(item, outputs, parent+'|#int#', tr , html, index)
    else:
        match = False
        name_t   = hstring.get_output_name(parent)
        parent_t = hstring.get_output_parent(parent)
        for tr_v in tr:
            if parent == tr_v and parent_t != 'root':
                index += 1
                if index != 1:
                    html += '</td></tr>'
                html  += '<tr><td>i is :' + str(index) +'</td><td>'
                break

        for item in outputs:
            if item['parent'] == parent_t and item['name'] == name_t:
                match = True
                html += item['cn_name'] + '(' + name_t + ')' + json + '<br>'
                break

        if match == False:
            html += parent + ':' + str(json) + '<br>'
    return [html, index]
