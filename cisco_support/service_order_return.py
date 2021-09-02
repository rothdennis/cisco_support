import requests
from cisco_support import utils

class RMA:

    __headers = None
    __verify = None
    __proxies = None

    def __init__(self, key: str, secret: str, verify: bool = True, proxies: dict = None) -> None:

        self.__verify = verify
        self.__proxies = proxies

        token = utils.getToken(key, secret, verify, proxies)      

        self.__headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }

    def getByRMANumber(self, rma_numbers: str) -> dict:
        params = {
        }

        url = f'https://api.cisco.com/return/v1.0/returns/rma_numbers/{rma_numbers}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByUserID(self, user_ids: str, fromDate: str = None, toDate: str = None, status: str = None, sortBy: str = 'orderdate') -> dict:
        params = {
            'fromDate': fromDate,
            'toDate': toDate,
            'status': status,
            'sortBy': sortBy
        }

        url = f'https://api.cisco.com/return/v1.0/returns/users/user_ids/{user_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()