# -*- coding: utf-8 -*-
import web

def getConnection():
    '''get connection of database'''
    db = web.database(dbn='mysql',db='Hiapi3',user='root',pw='password',host='localhost',port=3306);
    return db
