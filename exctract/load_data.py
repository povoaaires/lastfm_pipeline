from dotenv import load_dotenv
from datetime import date
from azure.storage.blob import BlobServiceClient
import json
import os


def SendLocal(load, name_file,path):
    with open(f"{path}{name_file}.json", "w") as file:
        json.dump(load,file)


        
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
    
