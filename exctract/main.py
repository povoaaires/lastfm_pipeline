import requests

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
    

