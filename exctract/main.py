import os
from dotenv import load_dotenv
import json
from get_data import *
from load_data import *

load_dotenv()

key_api = os.getenv("api_key")
app_api = os.getenv("app_project")
url_api = os.getenv("url_api")
path = os.getenv("path")

methods_general = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
methods_user = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
single = ['artist','track','tag']
plural = ['artists','tracks','tags']


for valor, general in enumerate(methods_general):
    req = ExtractGeneral(general, url_api, app_api, key_api)
    data = req.json()
    sing = single[valor]
    plur = plural[valor]
    data_resume = data[plur][sing]
    projeto = 'lastfm'
    categoria_nome = plur
    #load local
    SendLocal(data_resume,categoria_nome,'/data/raw')

    #load on cloud
    raw(projeto,categoria_nome,categoria_nome,data_resume)
    
