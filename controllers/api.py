#-*- coding:UTF-8 -*-
import web
from config import settings

render = settings.render
hiapi_db = settings.hiapi_db
data = {'page':'admin'}

class List:
    def GET(self):
        params = web.input()
        data["params"] = {}
        app_name = params.get("app_name","anjuke")
        version = params.get("version", "")
        sql = "SELECT i.id, i.name, i.version, i.method, i.category, i.is_login,ap.auto_type \
                FROM apis i \
                LEFT JOIN apps p on i.app_id = p.id \
                LEFT JOIN auto_param_inputs ap \
                on i.id = ap.api_id AND auto_type = 1 \
                WHERE p.name=$app_name "
        if version != "":
            sql += " AND i.version = $version"
        data["list"] = hiapi_db.query(sql, vars={"app_name": app_name, "version": version})
        data["select"] = get_select_info()
        data["params"] = {"app_name": app_name, "version": version}
        return render.apiList(data=data)

def get_select_info():
    apps = hiapi_db.query("SELECT DISTINCT name FROM apps ORDER BY name")
    apps = list(apps)
    versions = []
    for app in apps:
        version = hiapi_db.query("SELECT DISTINCT version FROM apis,apps \
                WHERE apis.app_id = apps.id AND apps.name=$app_name \
                ORDER BY version",vars={"app_name": app["name"]})
        versions.append(version)
    return [apps, versions]
