import requests
from . import auth

class ServiceOrderReturn:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/return/v1.0/returns'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_by_rma_number(self, rma_number):
        url = f'{self.base_url}/rma_numbers/{rma_number}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_by_user_id(self, user_id, from_date=None, to_date=None, status=None, sort_by='orderdate'):
        params = {
            'fromDate': from_date,
            'toDate': to_date,
            'status': status,
            'sortBy': sort_by
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        url = f'{self.base_url}/users/{user_id}'
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()