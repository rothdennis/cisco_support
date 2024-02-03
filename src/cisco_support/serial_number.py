import requests
from . import auth

class SerialNumberInformation:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/sn2info/v2'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_coverage_status_by_serial_numbers(self, serial_numbers):
        url = f"{self.base_url}/coverage/status/serial_numbers/{','.join(serial_numbers)}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_coverage_summary_by_serial_numbers(self, serial_numbers, page_index=1):
        params = {
            'page_index': page_index
        }
        url = f"{self.base_url}/coverage/summary/serial_numbers/{','.join(serial_numbers)}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_coverage_status_by_instance_numbers(self, instance_numbers, page_index=1):
        params = {
            'page_index': page_index
        }
        url = f"{self.base_url}/coverage/summary/instance_numbers/{','.join(instance_numbers)}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_orderable_product_ids_by_serial_numbers(self, serial_numbers):
        url = f"{self.base_url}/identifiers/orderable/serial_numbers/{','.join(serial_numbers)}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_owner_coverage_status_by_serial_numbers(self, serial_numbers):
        url = f"{self.base_url}/coverage/owner_status/serial_numbers/{','.join(serial_numbers)}"
        response = requests.get(url, headers=self.headers)
        return response.json()