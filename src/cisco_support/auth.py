import requests

def generate_access_token(client_id, client_secret):
    url = 'https://id.cisco.com/oauth2/default/v1/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)


    try:
        return response.json()['access_token']
    except:
        raise Exception(response.json()['errorSummary'])

