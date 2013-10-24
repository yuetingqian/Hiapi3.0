__author__ = 'yuetingqian'

from config.settings import render

class Index:
    def GET(self):
        name = 'yuetingqian'
        import web
        path = web.ctx.path
        path_list = path.split('/')
        if len(path_list) > 1:
            tag = path_list[1]
        else:
            tag = path_list[0]
        print path_list

        return render.index(name=name)
