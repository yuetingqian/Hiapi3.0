# -*- coding: utf-8 -*-
import web

def getConnection():
    '''get connection of database'''
    db = web.database(dbn='mysql',db='hiapi',user='root',pw='root',host='192.168.190.51',port=3306);
    return db
