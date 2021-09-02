import requests
from cisco_support import utils

class SS:

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

    def getSuggestedReleasesAndImagesByProductIDs(self, productIds: list, pageIndex: int = 1) -> dict:
        params = {
            'pageIndex': pageIndex
        }

        productIds = ','.join(productIds)

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/software/productIds/{productIds}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getSuggestedReleasesByProductIDs(self, productIds: list, pageIndex: int = 1) -> dict:
        params = {
            'pageIndex': pageIndex
        }

        productIds = ','.join(productIds)

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/releases/productIds/{productIds}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getCompatibleAndSuggestedSoftwareReleasesByProductID(self, productId: str, currentImage: str = None, currentRelease: str = None, pageIndex: int = 1, supportedFeatures: list = None, supportedHardware: list = None) -> dict:
        
        if supportedHardware:
            supportedHardware = '/'.join(supportedHardware)
        else:
            supportedHardware = None

        if supportedFeatures:
            supportedFeatures = ','.join(supportedFeatures)
        else:
            supportedFeatures = None
        
        params = {
            'currentImage': currentImage,
            'currentRelease': currentRelease,
            'supportedFeatures': supportedFeatures,
            'supportedHardware': supportedHardware,
            'pageIndex': pageIndex
        }

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/compatible/productId/{productId}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getSuggestedReleasesAndImagesByMDFIDs(self, mdfIds: list, pageIndex: int = 1) -> dict:
        params = {
            'pageIndex': pageIndex
        }

        mdfIds = ','.join(mdfIds)

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/software/mdfIds/{mdfIds}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getSuggestedReleasesByMDFIDs(self, mdfIds: list, pageIndex: int = 1) -> dict:
        params = {
            'pageIndex': pageIndex
        }

        mdfIds = ','.join(mdfIds)

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/releases/mdfIds/{mdfIds}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getCompatibleAndSuggestedSoftwareReleasesByMDFID(self, mdfId: str, currentImage: str = None, currentRelease: str = None, pageIndex: int = 1,supportedFeatures: list = None, supportedHardware: list = None) -> dict:
        
        if supportedHardware:
            supportedHardware = '/'.join(supportedHardware)
        else:
            supportedHardware = None

        if supportedFeatures:
            supportedFeatures = ','.join(supportedFeatures)
        else:
            supportedFeatures = None
        
        params = {
            'pageIndex': pageIndex,
            'currentImage': currentImage,
            'currentRelease': currentRelease,
            'supportedFeatures': supportedFeatures,
            'supportedHardware': supportedHardware
        }

        url = f'https://api.cisco.com/software/suggestion/v2/suggestions/compatible/mdfId/{mdfId}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()