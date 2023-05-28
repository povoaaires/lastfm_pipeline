import os
from dotenv import load_dotenv
import json
import exctract.get_data as ex
#from datetime import date
#from azure.storage.blob import BlobServiceClient
import json




load_dotenv()

key_api = os.getenv("api_key")
app_api = os.getenv("app_project")
url_api = os.getenv("url_api")
path = os.getenv("path")

methods_general = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
methods_user = ['chart.gettopartists','chart.gettoptracks','chart.gettoptags']
#exctract
r = ex.ExtractGeneral(methods_general[0], url_api, app_api, key_api)


#main
artistas = r.json()
artistas_exctraction = artistas['artists']['artist']



#load
projeto = 'lastfm'
categoria = 'artista'
nome = 'teste'


def raw(projeto,categoria,nome,dado):
    year = date.today().strftime('%Y')
    month = date.today().strftime('%m')
    day = date.today().strftime('%d')
    
    #Infos para Autenticação
    account_name = os.getenv("account_name")
    account_key = os.getenv("account_key")
    container_name = 'raw'
    blob_name = f'{projeto}/{categoria}/{year}/{month}/{day}/{nome}.json'
    
    #Criação Cliente
    try:
        blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net")
        print("Conexão realizada com Sucesso!")
    except Exception as ex:
        print(f"Erro na autenticação com o ADLS: {ex}")
        
    # Escrever o conteúdo JSON no arquivo
    try:
        json_content = json.dumps(dado)
        print("Dado transformado para JSON")
        
    except Exception as ex:
        print(f"Erro ao transformar o dado em JSON: {ex}")
        
    try:
        container_client = blob_service_client.get_container_client(container_name)
        container_client.upload_blob(name=blob_name, data=json_content, overwrite=True)
        print("Dado carregado com sucesso na camada Raw")
    except Exception as ex:
        print(f"Erro ao carregar o dado: {ex}")
    

raw(projeto,categoria,nome,artistas_exctraction)

