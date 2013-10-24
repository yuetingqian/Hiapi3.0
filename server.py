__author__ = 'yuetingqian'

#!/usr/bin/python
import web
from config.url import urls
app = web.application(urls, globals())
def notfound():
    return web.seeother('/404')
app.notfound = notfound

if __name__ == "__main__":
    app.run()



