from azure.storage.blob import BlobServiceClient
import pandas as pd
from datetime import date
import os
from io import BytesIO


year = date.today().strftime('%Y')
month = date.today().strftime('%m')
day = date.today().strftime('%d')
projeto = 'lastfm'
categoria = 'artista'
nome = 'teste'
account_name = os.getenv("account_name")
account_key = os.getenv("account_key")
container_name = 'raw'
blob_name = f'{projeto}/{categoria}/{year}/{month}/{day}/{nome}.json'


blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net")

#ler um json da Raw
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
file_contents = blob_client.download_blob().readall()
df = pd.read_json(BytesIO(file_contents))
print(df)
