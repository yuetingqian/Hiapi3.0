# -*- coding: utf-8 -*-
import sys
sys.path.append('../config')
path = sys.path
from config import settings

hiapi_db = settings.hiapi_db

def get_apps():
    return hiapi_db.select('apps')
