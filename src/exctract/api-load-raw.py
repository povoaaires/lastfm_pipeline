import requests
import json


API_KEY = '925252b2baf7b11b361e8569bf9cafab'
USER_AGENT = 'app_project'

headers = {
    'user-agent': USER_AGENT
}

payload = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(r)


j = r.json()
text = json.dumps(j, sort_keys=True, indent=4)
print(text)
