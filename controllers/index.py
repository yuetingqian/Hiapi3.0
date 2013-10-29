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
        from dao import query
        app = list(query.get_apps())
        for i in app:
            print i
        print app[0]
        print type(app)
        return render.index(name=name,app=app)
