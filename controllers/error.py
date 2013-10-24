__author__ = 'yuetingqian'

from config.settings import render

class NotFound:
    def GET(self):
        return render.notfound()
