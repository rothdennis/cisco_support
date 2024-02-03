import requests
from . import auth

class Case:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/case/v3/cases'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_summary_by_ids(self, case_ids, sort_by='STATUS'):
        url = f"{self.base_url}/case_ids/{','.join(case_ids)}?sort_by={sort_by}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_details_by_id(self, case_id):
        url = f"{self.base_url}/details/case_id/{case_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_by_contract_ids(self, contract_ids, date_created_from=None, date_created_to=None, status_flag=None, sort_by='UPDATED_DATE', page_index=1):
        params = {
            'date_created_from': date_created_from,
            'date_created_to': date_created_to,
            'status_flag': status_flag,
            'sort_by': sort_by,
            'page_index': page_index
        }
        # remove None values
        params = {k: v for k, v in params.items() if v is not None}

        url = f"{self.base_url}/contracts/contract_ids/{','.join(contract_ids)}?{requests.compat.urlencode(params)}"
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_by_user_ids(self, user_ids, date_created_from=None, date_created_to=None, status_flag=None, sort_by='UPDATED_DATE', page_index=1):
        params = {
            'date_created_from': date_created_from,
            'date_created_to': date_created_to,
            'status_flag': status_flag,
            'sort_by': sort_by,
            'page_index': page_index
        }
        # remove None values
        params = {k: v for k, v in params.items() if v is not None}

        url = f"{self.base_url}/users/user_ids/{','.join(user_ids)}?{requests.compat.urlencode(params)}"
        response = requests.get(url, headers=self.headers)
        return response.json()