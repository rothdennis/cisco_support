import requests
from . import auth

class SoftwareSuggestion:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/software/suggestion/v2/suggestions'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_suggested_releases_and_images_by_pid(self, pids, page_index=1):
        params = {
            'pageIndex': page_index,
        }
        url = f"{self.base_url}/software/productIds/{','.join(pids)}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_suggested_releases_by_pid(self, pids, page_index=1):
        params = {
            'pageIndex': page_index,
        }
        url = f"{self.base_url}/releases/productIds/{','.join(pids)}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_compatible_and_suggested_software_release_by_pid(self, pid, current_image=None, current_release=None, page_index=1, supported_features=None, supported_hardware=None):
        params = {
            'pageIndex': page_index,
            'currentImage': current_image,
            'currentRelease': current_release
        }
        if supported_features:
            params['supportedFeatures'] = ','.join(supported_features)
        if supported_hardware:
            params['supportedHardware'] = ','.join(supported_hardware)
        # remove all None values from params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/compatible/productId/{pid}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_suggested_releases_and_images_by_mdf_ids(self, mdf_ids, page_index=1):
        params = {
            'pageIndex': page_index,
        }
        url = f"{self.base_url}/software/mdfIds/{','.join(mdf_ids)}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_suggested_releases_by_mdf_ids(self, mdf_ids, page_index=1):
        params = {
            'pageIndex': page_index,
        }
        url = f"{self.base_url}/releases/mdfIds/{','.join(mdf_ids)}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_compatible_and_suggested_software_releases_by_mdf_id(self, mdf_is, current_image=None, current_release=None, page_index=1, supported_features=None, supported_hardware=None):
        params = {
            'pageIndex': page_index,
            'currentImage': current_image,
            'currentRelease': current_release
        }
        if supported_features:
            params['supportedFeatures'] = ','.join(supported_features)
        if supported_hardware:
            params['supportedHardware'] = ','.join(supported_hardware)
        # remove all None values from params
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/compatible/mdfId/{mdf_is}?pageIndex={page_index}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()