# -*- coding: utf-8 -*-
def get_output_name(str):
    name = ''
    str_list = str.split('|')
    strlen = len(str_list)

    if strlen > 1:
        name = str_list[strlen-1]

    return name

def get_output_parent(str):
    pos = len(get_output_name(str)) + 1
    parent = str[:-pos]
    return parent
