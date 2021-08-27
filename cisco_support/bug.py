import requests
from cisco_support import utils

class Bug:

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

    def getByIDs(self, bug_ids: list) -> dict:
        params = {}

        bug_ids = ','.join(bug_ids)

        url = f'https://api.cisco.com/bug/v2.0/bugs/bug_ids/{bug_ids}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByBaseProductIDs(self, base_pid: str, page_index: int = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/products/product_id/{base_pid}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByBaseProductIDsAndSoftwareReleases(self, base_pid: str, software_releases: str, page_index: int = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/products/product_id/{base_pid}/software_releases/{software_releases}'

        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByKeywords(self, keyword: list, page_index: int = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        keyword = ','.join(keyword)

        url = f'https://api.cisco.com/bug/v2.0/bugs/keyword/{keyword}'
        
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductSeriesAndAffectedSoftwareRelease(self, product_series: str, affected_releases: list, page_index: int = 1, status: str = None, modified_date: str = None, severity: str = None, sort_by: str = None) -> dict:
        affected_releases = ','.join(affected_releases)
        
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/product_series/{product_series}/affected_releases/{affected_releases}'
        
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductSeriesAndFixedInSoftwareRelease(self, product_series: str, fixed_in_releases: list, page_index: str = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        fixed_in_releases = ','.join(fixed_in_releases)
        
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/product_series/{product_series}/fixed_in_releases/{fixed_in_releases}'
        
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductNameAndAffectedSoftwareRelease(self, product_name: str, affected_releases: list, page_index: str = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        affected_releases = ','.join(affected_releases)
        
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/product_name/{product_name}/affected_releases/{affected_releases}'
        
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductNameAndFixedInSoftwareRelease(self, product_name: str, fixed_in_releases: list, page_index: str = 1, status: str = None, modified_date: str = 2, severity: str = None, sort_by: str = None) -> dict:
        fixed_in_releases = ','.join(fixed_in_releases)
        
        params = {
            'page_index': page_index,
            'modified_date': modified_date,
            'status': status,
            'severity': severity,
            'sort_by': sort_by
        }

        url = f'https://api.cisco.com/bug/v2.0/bugs/product_name/{product_name}/fixed_in_releases/{fixed_in_releases}'
        
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()
