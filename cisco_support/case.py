import requests
import json
from cisco_support import utils

class Case:

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
        }

    def getCaseSummary(self, case_ids: list, sort_by: str = 'UPDATED_DATE') -> dict:
        params = {
            'sort_by': sort_by
        }

        case_ids = ','.join(case_ids)

        url = f'https://api.cisco.com/case/v3/cases/case_ids/{case_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        print(r.content)

        return r.json()

    def getCaseDetails(self, case_id: str) -> dict:
        params = {}

        url = f'https://api.cisco.com/case/v3/cases/details/case_id/{case_id}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByContractID(self, contract_ids: list, date_created_from: str, date_created_to: str, status_flag: str = 'O', sort_by: str = 'UPDATED_DATE', page_index: int = 1) -> dict:
        params = {
            'date_created_from': date_created_from,
            'date_created_to': date_created_to,
            'sort_by': sort_by,
            'status_flag': status_flag,
            'page_index': page_index
        }

        contract_ids = ','.join(contract_ids)

        url = f'https://api.cisco.com/case/v3/cases/contracts/contract_ids/{contract_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByUserID(self, user_ids: list, date_created_from: str = None, date_created_to: str = None, status_flag: str = 'O', sort_by: str = 'UPDATED_DATE', page_index: int = 1) -> dict:
        params = {
            'date_created_from': date_created_from,
            'date_created_to': date_created_to,
            'sort_by': sort_by,
            'status_flag': status_flag,
            'page_index': page_index
        }

        user_ids = ','.join(user_ids)

        url = f'https://api.cisco.com/case/v3/cases/users/user_ids/{user_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()