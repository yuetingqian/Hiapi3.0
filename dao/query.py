# -*- coding: utf-8 -*-
import sys
sys.path.append('../config')
path = sys.path
from config import settings
from helpers import htime
hiapi_db = settings.hiapi_db

def get_apps():
    return hiapi_db.select('apps')

def get_inputs(api_id):
    inputs = hiapi_db.select('param_inputs',where='api_id=$api_id',vars={'api_id':api_id})
    return inputs

def get_outputs(api_id):
    outputs = hiapi_db.select('param_outputs',where='api_id=$api_id',vars={'api_id':api_id})
    return list(outputs)

def add_outputs(value):
    if 'cn_name' not in value:
        value['cn_name'] = ''
    now = htime.get_now()
    hiapi_db.insert('param_outputs', name=value['name'], cn_name=value['cn_name'], type=value['type'],
            parent=value['parent'],api_id=value['api_id'],updated_at=now)
