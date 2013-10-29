# -*- coding: utf-8 -*-
def get_output_name(str):
    name = ''
    str_list = str.split('|')
    len = len(str_list)

    if len > 1:
        name = str_list[len-1]

    return name

def get_output_parent(str):
    pos = len(get_output_name(str))
    parent = str[:-pos]
    return parent
