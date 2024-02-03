import requests
from . import auth

class Bug:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/bug/v2.0/bugs'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_by_ids(self, bug_ids):
        url = f"{self.base_url}/bug_ids/{','.join(bug_ids)}"
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_by_product_id(self, product_id, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/products/product_id/{product_id}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_pid_and_software_release(self, pid, software_release, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/products/product_id/{pid}/software_releases/{software_release}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_keywords(self, keywords, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/keyword/{' '.join(keywords)}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_product_series_and_affected_software_release(self, product_series, affected_releases, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/product_series/{product_series}/affected_releases/{affected_releases}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_product_series_and_fixed_in_software_release(self, product_series, fixed_in_releases, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/product_series/{product_series}/fixed_in_releases/{fixed_in_releases}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_product_name_and_affected_software_release(self, product_name, affected_releases, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/product_name/{product_name}/affected_releases/{affected_releases}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_by_product_name_and_fixed_in_software_release(self, product_name, fixed_in_releases, page_index=1, status=None, modified_date=None, severity=None, sort_by=None):
        params = {
            'page_index': page_index,
            'status': status,
            'modified_date': modified_date,
            'severity': severity,
            'sort_by': sort_by
        }
        # Remove any None values from the params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/product_name/{product_name}/fixed_in_releases/{fixed_in_releases}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()