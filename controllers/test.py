__author__ = 'yuetingqian'

from config.settings import render

class Index:
    def GET(self):
        return render.test()
