__author__ = 'yuetingqian'

#!/usr/bin/python
import web
urls = (
    '/','Index'
)

class Index:
    def GET(self):
        return "111Hello"



app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()