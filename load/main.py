import json
import os
from dotenv import load_dotenv
from datetime import date
from azure.storage.blob import BlobServiceClient


load_dotenv()

def SendLocal(load, name_file,path):
    with open(f"{path}{name_file}.json", "w") as file:
        json.dump(load,file)
        


    
    