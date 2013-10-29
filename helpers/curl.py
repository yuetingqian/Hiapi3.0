# -*- coding: utf-8 -*-
import pycurl
import StringIO

def curl_get(url):
    curl = pycurl.Curl()
    curl.setopt(pycurl.VERBOSE, 1)
#    curl.setopt(pycurl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.HTTPHEADER, ['Content-type:text/xml','charset:utf-8'])
    curl.setopt(pycurl.CONNECTTIMEOUT, 60)
    curl.setopt(pycurl.TIMEOUT, 60)
    curl.setopt(pycurl.URL, url)
    storage = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, storage.write)
#    curl.setopt(pycurl.HEADERFUNCTION, storage.write)
    curl.perform()
    curl.close()
    json = storage.getvalue()
    return json
