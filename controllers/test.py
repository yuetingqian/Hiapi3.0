__author__ = 'yuetingqian'
import json
from config.settings import render
from dao import query
from helpers import curl, myjson

class Index:
    def GET(self):

        inputs = query.get_inputs(1)
        for item in inputs:
            print item
        outputs = query.get_outputs(1)

        url = 'http://api.anjuke.com/mobile/1.3/property.searchV3?api_key=ef7545201a2bc5911cdb43527b18b8c1&city_id=11&page_size=2&uuid=dev22&sig=5f755b7c1ab67828805be20d625b9e47'
        sjson = curl.curl_get(url)
        djson = json.loads(sjson)
        myjson.parser(djson,outputs)

        return render.test(json=sjson)
