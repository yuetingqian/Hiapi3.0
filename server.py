__author__ = 'yuetingqian'

#!/usr/bin/python
import web
from config.url import urls
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()



