import requests
from . import auth

class ProductInformation:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = "https://apix.cisco.com/product/v1/information"
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_by_serial_numbers(self, serial_numbers, pageIndex=1):
        url = f"{self.base_url}/serial_numbers/{','.join(serial_numbers)}?responseencoding=json&page_index={pageIndex}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_by_product_ids(self, product_ids, pageIndex=1):
        url = f"{self.base_url}/product_ids/{','.join(product_ids)}?responseencoding=json&page_index={pageIndex}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_mdf_by_ids(self, product_ids, pageIndex=1):
        url = f"{self.base_url}/mdf/product_ids_mdf/{','.join(product_ids)}?responseencoding=json&page_index={pageIndex}"
        response = requests.get(url, headers=self.headers)
        return response.json()