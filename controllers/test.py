__author__ = 'yuetingqian'
import json
from config.settings import render
from dao import query
from helpers import hcurl, hjson
import collections

class Index:
    def GET(self):

        inputs = query.get_inputs(1)
        for item in inputs:
            print item
        outputs = query.get_outputs(1)

        #url = 'http://api.anjuke.com/mobile/1.3/property.searchV3?api_key=ef7545201a2bc5911cdb43527b18b8c1&city_id=11&page_size=2&uuid=dev22&sig=5f755b7c1ab67828805be20d625b9e47'
        url = 'http://api.anjuke.com/mobile/1.3/property.searchV3?api_key=ef7545201a2bc5911cdb43527b18b8c1&city_id=11&page_size=5&uuid=dev22&sig=6a1931899824443142db4a4cc6bd70f2'
        sjson = hcurl.curl_get(url)
        djson = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(sjson)
        djson = json.loads(sjson, object_pairs_hook=collections.OrderedDict)
        re = hjson.parser(outputs, djson, ['root|properties|#int#|id','root|total'],1)

        return render.test(json=re[0],error=re[1])
