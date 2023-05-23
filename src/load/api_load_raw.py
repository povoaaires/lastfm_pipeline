import requests
import os
from dotenv import load_dotenv
import json
import sys
from src.exctract.funcoes_extracao import ExtractGeneral







load_dotenv()

key_api = os.getenv("api_key")
app_api = os.getenv("app_project")
url_api = os.getenv("url_api")
path = os.getenv("path")

methods_general = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
methods_user = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']

r = ExtractGeneral(methods_general[0], url_api, app_api, key_api)

artistas = r.json()
artistas_exctraction = artistas['artists']['artist']
# #json_objeto = json.dumps(artistas_exctraction,ident=4)
# with open(f"{path}artistas.json", "w") as file:
#     json.dump(artistas_exctraction,file)