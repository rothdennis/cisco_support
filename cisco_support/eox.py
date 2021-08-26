import requests

class EoX:

    __headers = None

    def __init__(self, key, secret):

        token = self.__getToken(key, secret)      

        self.__headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }

    def __getToken(self, client_id, client_secret) -> str:

        url = 'https://cloudsso.cisco.com/as/token.oauth2'

        params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }

        r = requests.post(url=url, params=params, headers=headers)

        return r.json()['access_token']


    def getByDates(self, startDate, endDate, pageIndex):
        
        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXByDates/{pageIndex}/{startDate}/{endDate}'

        r = requests.get(url=url, headers=self.__headers)

        return r.json()

    def getByProducsIDs(self):
        pass

    def getBySerialNumbers(self):
        pass

    def getBySoftwareReleaseStrings(self):
        pass