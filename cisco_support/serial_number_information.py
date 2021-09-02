import requests
from cisco_support import utils

class SNI:

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

    def getCoverageStatusBySerialNumbers(self, sr_no: list) -> dict:
        params = {
        }

        sr_no = ','.join(sr_no)

        url = f'https://api.cisco.com/sn2info/v2/coverage/status/serial_numbers/{sr_no}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def  getCoverageSummaryByInstanceNumbers(self, instance_no: list, page_index: int = 1) -> dict:
        params = {
            'page_index': page_index
        }

        instance_no = ','.join(instance_no)

        url = f'https://api.cisco.com/sn2info/v2/coverage/summary/instance_numbers/{instance_no}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getCoverageSummaryBySerialNumbers(self, sr_no: list, page_index: int = 1) -> dict:
        params = {
            'page_index': page_index
        }

        sr_no = ','.join(sr_no)

        url = f'https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/{sr_no}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getOrderableProductIDsBySerialNumbers(self, sr_no: list) -> dict:
        params = {
        }

        sr_no = ','.join(sr_no)

        url = f'https://api.cisco.com/sn2info/v2/identifiers/orderable/serial_numbers/{sr_no}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getOwnerCoverageStatusBySerialNumbers(self, sr_no: list) -> dict:
        params = {
        }

        sr_no = ','.join(sr_no)

        url = f'https://api.cisco.com/sn2info/v2/coverage/owner_status/serial_numbers/{sr_no}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()