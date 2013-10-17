__author__ = 'yuetingqian'

from config.settings import render

class Index:
    def GET(self):
        name = 'yuetingqian'
        return render.index(name=name)
