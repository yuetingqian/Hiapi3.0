# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from helpers import hstring
from dao import query

parent = 'root'
tr = []
def parser(api_id, outputs, json, parent=parent, tr=tr, is_insert=False, html='', index=0):
    #outputs = query.get_outputs(api_id)
    if isinstance(json, dict):
        for key in json:
            [html, outputs, index] = parser(api_id, outputs, json[key], parent+'|'+key, tr, is_insert, html, index)
    elif isinstance(json, list):
        for item in json:
            [html, outputs, index] = parser(api_id, outputs, item, parent+'|#int#', tr , is_insert, html, index)
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

        sjson = str(json)
        cn_name = ''
        for item in outputs:
            if item['parent'] == parent_t and item['name'] == name_t:
                match = True
                cn_name = item['cn_name']
                break

        if match == False and parent != 'root|status':
            if is_insert != True:
                html += '<font color="red">数据库字段缺失：</font>' + parent + ':' + sjson + '<br>'
            else:
                output = {
                        'name'   : name_t,
                        'type'   : type(json).__name__,
                        'parent' : parent_t,
                        'api_id' : api_id,
                        }
                query.add_outputs(output)
                outputs = query.get_outputs(api_id)

        if match == True or is_insert == True:
            html_t = cn_name
            if name_t != '#int#':
                html_t += '(' + name_t + '):'

            if parent_t == 'root':
                html += '<tr><td>' + cn_name + '(' + name_t + ')</td><td>' + sjson + '</td></tr>'
            else:
                if sjson[-4:] in ['.jpg', '.png', '.bmp']:
                    html += html_t + '<img src=' + sjson + '>'
                else:
                    html += html_t + sjson
                html += '<br>'

    return [html, outputs, index]
