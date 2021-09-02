import requests
from cisco_support import utils

class PI:

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

    def getBySerialNumbers(self, serial_numbers: list, page_index: int = 1) -> dict:
        params = {
            'page_index': page_index
        }

        serial_numbers = ','.join(serial_numbers)

        url = f'https://api.cisco.com/product/v1/information/serial_numbers/{serial_numbers}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductIDs(self, product_ids: list, page_index: int = 1) -> dict:
        params = {
            'page_index': page_index
        }

        product_ids = ','.join(product_ids)

        url = f'https://api.cisco.com/product/v1/information/product_ids/{product_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getMDFInformationByProductIDs(self, product_ids: list, page_index: int = 1) -> dict:
        params = {
            'page_index': page_index
        }

        product_ids = ','.join(product_ids)

        url = f'https://api.cisco.com/product/v1/information/product_ids/{product_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()