# -*- coding: utf-8 -*-
from helpers import mystring

parent = 'root'

def parser(json, outputs, parent=parent):
    if isinstance(json, dict):
        for i in json:
            parser(json[i], outputs, parent+'|'+i)
    elif isinstance(json, list):
        for item in json:
            parser(item, outputs, parent+'|#int#')
    else:
        match = False
        for item in outputs:
            if item['parent']+'|'+item['name'] == parent:
                match = True
                print '(',  item['cn_name'], ')',parent,':',json
                break
        if match == False:
            print parent,':',json
    return json
