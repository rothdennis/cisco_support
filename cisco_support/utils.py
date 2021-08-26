import requests

def getToken(client_id: str, client_secret: str, verify: bool, proxies: dict) -> str:
        url = 'https://cloudsso.cisco.com/as/token.oauth2'

        params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }

        r = requests.post(url=url, params=params, headers=headers, verify=verify, proxies=proxies)
        return r.json()['access_token']