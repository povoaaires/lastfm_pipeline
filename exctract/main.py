import os
from dotenv import load_dotenv
import json
import exctract.get_data as get
import exctract.load_data as load

load_dotenv()

key_api = os.getenv("api_key")
app_api = os.getenv("app_project")
url_api = os.getenv("url_api")
path = os.getenv("path")

methods_general = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
methods_user = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
#exctract
r = get.ExtractGeneral(methods_general[0], url_api, app_api, key_api)


#main
artistas = r.json()
artistas_exctraction = artistas['artists']['artist']

projeto = 'lastfm'
categoria = 'artista'
nome = 'artistas'

#load local
load.SendLocal(artistas_exctraction,nome,path)

#load on cloud
load.raw(projeto,categoria,nome,artistas_exctraction)