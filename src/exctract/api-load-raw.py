import requests
import os
from dotenv import load_dotenv
import json



load_dotenv()

key_api = os.getenv("api_key")
app_api = os.getenv("app_project")
url_api = os.getenv("url_api")
path = os.getenv("path")

methods_general = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
methods_user = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']


def ExtractGeneral(general, url, app, key):
    
    headers = {
        'user-agent': app
    }
    
    body = {
        'api_key': key,
        'method': general,
        'format': 'json'
    }
    
    try:
        request = requests.get(url, headers=headers, params=body)
    except Exception as ex:
        print(ex)
    
    return request


def ExtractUser(user_method,user, url, app, key):
    
    headers = {
        'user-agent': app
    }
    
    body = {
        'api_key': key,
        'method': user_method,
        'user': user,
        'format': 'json'
    }
    try:
        request = requests.get(url, headers=headers, params=body)
    except Exception as ex:
        print(ex)
        
    return request
    



r = ExtractGeneral(methods_general[0], url_api, app_api, key_api)

artistas = r.json()
artistas_exctraction = artistas['artists']['artist']
#json_objeto = json.dumps(artistas_exctraction,ident=4)
with open(f"{path}artistas.json", "w") as file:
    json.dump(artistas_exctraction,file)
    
    
#print(artistas_exctraction)


# text = json.dumps(j, sort_keys=True, indent=4)
# print(text)
