# -*- coding: utf-8 -*-
import sys
sys.path.append('../config')
path = sys.path
from config import settings

hiapi_db = settings.hiapi_db

def get_apps():
    return hiapi_db.select('apps')

def get_inputs(api_id):
    inputs = hiapi_db.select('param_inputs',where='api_id=$api_id',vars={'api_id':api_id})
    return inputs

def get_outputs(api_id):
    outputs = hiapi_db.select('param_outputs',where='api_id=$api_id',vars={'api_id':api_id})
    return list(outputs)
