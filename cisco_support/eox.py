import requests

class EoX:

    __headers = None
    __verify = None
    __proxies = None

    def __init__(self, key: str, secret: str, verify: bool = True, proxies: dict = None) -> None:

        self.__verify = verify
        self.__proxies = proxies

        token = self.__getToken(key, secret)      

        self.__headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }

    def __getToken(self, client_id: str, client_secret: str) -> str:
        url = 'https://cloudsso.cisco.com/as/token.oauth2'

        params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }

        r = requests.post(url=url, params=params, headers=headers, verify=self.__verify, proxies=self.__proxies)
        return r.json()['access_token']

    def getByDates(self, startDate:str, endDate: str, pageIndex: int = 1, eoxAttrib: list = []) -> dict:

        params = {
            'eoxAttrib': ','.join(eoxAttrib),
            'responseencoding': 'json'
        }

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXByDates/{pageIndex}/{startDate}/{endDate}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProducsIDs(self, productID: list, pageIndex: int = 1):
        params = {
            'responseencoding': 'json'
        }

        productID = ','.join(productID)

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/{pageIndex}/{productID}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getBySerialNumbers(self,serialNumber: list , pageIndex: int = 1):
        params = {
            'responseencoding': 'json'
        }

        serialNumber = ','.join(serialNumber)

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/{pageIndex}/{serialNumber}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getBySoftwareReleaseStrings(self, software: list , pageIndex:int = 1):
        params = {
            'responseencoding': 'json'
        }

        for i, sw in enumerate(software):
            params.update({
                f'input{i+1}': sw
            })

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXBySWReleaseString/{pageIndex}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()