# -*- coding:utf-8 -*-
import time

def get_now():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
