import requests
from . import auth

class EoX:
    def __init__(self, client_id, client_secret, proxies=None, verify=True):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = "https://apix.cisco.com/supporttools/eox/rest/5"
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        self.proxies = proxies
        self.verify = verify

    def get_by_dates(self, start_date, end_date, page_index=1):
        url = f"{self.base_url}/EOXByDates/{page_index}/{start_date}/{end_date}?responseencoding=json"
        response = requests.get(url, headers=self.headers, verify=self.verify, proxies=self.proxy)
        return response.json()

    def get_by_product_ids(self, product_ids, page_index=1):
        url = f"{self.base_url}/EOXByProductID/{page_index}/{','.join(product_ids)}?responseencoding=json"
        response = requests.get(url, headers=self.headers, verify=self.verify, proxies=self.proxy)
        return response.json()

    def get_by_serial_numbers(self, serial_numbers, page_index=1):
        url = f"{self.base_url}/EOXBySerialNumber/{page_index}/{','.join(serial_numbers)}?responseencoding=json"
        response = requests.get(url, headers=self.headers, verify=self.verify, proxies=self.proxy)
        return response.json()

    def get_by_software_release_strings(self, softwares, page_index=1):
        sw = []
        for i, software in enumerate(softwares):
            sw.append(f"input{i+1}={software}")
        url = f"{self.base_url}/EOXBySWReleaseString/{page_index}?{'&'.join(sw)}&responseencoding=json"
        response = requests.get(url, headers=self.headers, verify=self.verify, proxies=self.proxy)
        return response.json()