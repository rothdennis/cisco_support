import requests
import json
from cisco_support import utils

class ASD:

    __headers = None
    __verify = None
    __proxies = None

    def __init__(self, key: str, secret: str, verify: bool = True, proxies: dict = None) -> None:

        self.__verify = verify
        self.__proxies = proxies

        token = utils.getToken(key, secret, verify, proxies)      

        self.__headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def getByProductIDAndRelease(self, pid: str, currentReleaseVersion: str, outputReleaseVersion: str = 'latest', pageIndex: int = 1, perPage: int = 25) -> dict:
        
        data = {
            "pid": pid,
            "currentReleaseVersion": currentReleaseVersion,
            "outputReleaseVersion": outputReleaseVersion,
            "pageIndex": pageIndex,
            "perPage": perPage
        }
        
        url = 'https://api.cisco.com/software/v4.0/metadata/pidrelease'

        r = requests.post(url=url, params=data, headers=self.__headers, verify=self.__verify, proxies=self.__proxies)

        print(r.content)

        return r.json()



    def getByProductIDAndImage(self) -> dict:
        pass