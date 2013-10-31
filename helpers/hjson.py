# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from helpers import hstring
from dao import query

parent = 'root'
tr = []
def parser(outputs, json, parent=parent, tr=tr, api_id=0, html='',error='', index=0):
    if isinstance(json, dict):
        for key in json:
            [html, error, outputs, index] = parser(outputs, json[key], parent+'|'+key, tr, api_id, html, error, index)
    elif isinstance(json, list):
        for item in json:
            [html, error, outputs, index] = parser(outputs, item, parent+'|#int#', tr , api_id, html, error, index)
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

        cn_name    = ''
        error_type = ''
        error_lack = ''
        sjson      = str(json)
        json_type = type(json.encode('utf-8')).__name__ if type(json).__name__ =='unicode' else type(json).__name__
        db_type = json_type
        for item in outputs:
            if item['parent'] == parent_t and item['name'] == name_t:
                match = True
                cn_name = item['cn_name']
                db_type = item['type']
                break

        if match == False and parent != 'root|status':
            if api_id == 0:
                error_lack = '<font color="red">数据库字段缺失：</font>' + parent + ':' + sjson + '<br>'
                error  += error_lack
                html   += error_lack
            else:
                output = {
                        'name'   : name_t,
                        'type'   : json_type,
                        'parent' : parent_t,
                        'api_id' : api_id,
                        }
                query.add_outputs(output)
                outputs = query.get_outputs(api_id)

        if match == True or api_id > 0:
            html_t = cn_name
            if name_t != '#int#':
                html_t += '(' + name_t + '):'

            if db_type != json_type :
                error_type = '<font color="red">(' + parent + '数据类型错误，expect='+ item['type'] + ',actual=' + json_type + ')</font>'
                error  += error_type + '<br>'

            if parent_t == 'root':
                html += '<tr><td>' + cn_name + '(' + name_t + ')</td><td>' + sjson + error_type+ '</td></tr>'
            else:
                if sjson[-4:] in ['.jpg', '.png', '.bmp']:
                    html += html_t + '<img src=' + sjson + '>'
                else:
                    html += html_t + sjson
                html += error_type +'<br>'

    return [html, error, outputs, index]
