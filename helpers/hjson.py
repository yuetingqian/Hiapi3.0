# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from helpers import hstring
from dao import query

parent = 'root'
tr = []
def parser(outputs, json,tr=tr, api_id=0, parent=parent, html='',error='', index=0):
    '''

    用来返回json解析结果或者插入json的函数，若只需要展示，只需填入前三个参数
    outputs  params_outputs中api返回参数
    json     curl api后json.loads后的结果
    tr       apis表中tr
    api_id   当该参数大于0时，若param_outputs中没有可自动插入json里的返回值
    parent   一般是root
    html     展示的html
    error    解析过程中的报错，包括字段缺失，类型不符等
    index    表示结果序号，比如第几套房源

    逻辑如下：
    1.如果json类型是dict或者list说明没到叶子节点，继续递归
    2.否则先检测当前节点是否是分割符节点
      然后检测db里是否有该节点记录，如果没有并且不是root|status，并且api_id为0就报错，如果api_id不是0就插入
      如果db有该节点或者api_id大于0，则检查其类型并展示

    '''
    if isinstance(json, dict):
        for key in json:
            [html, error, outputs, index] = parser(outputs, json[key],tr, api_id, parent+'|'+key, html, error, index)
    elif isinstance(json, list):
        for item in json:
            [html, error, outputs, index] = parser(outputs, item, tr, api_id, parent+'|#int#', html, error, index)
    else:
        match = False
        name_t   = hstring.get_output_name(parent)
        parent_t = hstring.get_output_parent(parent)
        for tr_v in tr:
            if parent == tr_v and parent_t != 'root':
                index += 1
                if index != 1:
                    html += '</td></tr>'
                html  += '<tr><td>' + str(index) +'</td><td>'
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
                error_lack = '<font color="red">数据库字段缺失：</font>' + parent + '<br>'
                if parent_t == 'root':
                    error_lack = '<tr><td></td><td>%s</td><tr>'% error_lack
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

        if parent!='root|status' and (match == True or api_id > 0):
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
