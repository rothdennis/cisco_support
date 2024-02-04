import requests
import json
from . import auth

class AutomatedSoftwareDistribution:

    def __init__(self, client_id, client_secret):
        self.access_token = auth.generate_access_token(client_id, client_secret)
        self.base_url = 'https://apix.cisco.com/software/v4.0'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }


    def get_software_release_by_pid_and_release(self, pid, current_release_version, output_release_version, page_index=1, per_page=25):
        data = {
            'pid': pid,
            'currentReleaseVersion': current_release_version,
            'OutputReleaseVersion': output_release_version,
            'pageIndex': page_index,
            'perPage': per_page

        }
        url = f"{self.base_url}/metadata/pidrelease"
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        try:
            return response.json()
        except:
            raise Exception(f'{response.status_code} - {response.text}')