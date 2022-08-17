import requests
from cisco_support import utils

class EoX:

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

    def getByDates(self, startDate:str, endDate: str, pageIndex: int = 1, eoxAttrib: list = []) -> dict:
        """getByDates

        Args:
            startDate (str):Start date of the date range of records to return in the following format: YYYY-MM-DD. For example: 2010-01-01
            endDate (str): End date of the date range of records to return in the following format: YYYY-MM-DD. For example: 2010-01-01
            pageIndex (int, optional): Index number of the page to return; a maximum of 50 records per page are returned. Defaults to 1.
            eoxAttrib (list, optional): Attribute or attributes of the records to return. Enter multiple values separated by commas. Defaults to [].

        Returns:
            dict: {PaginationResponseRecord, EOXRecord}
        """
        params = {
            'eoxAttrib': ','.join(eoxAttrib),
            'responseencoding': 'json'
        }

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXByDates/{pageIndex}/{startDate}/{endDate}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getByProductIDs(self, productID: list, pageIndex: int = 1) -> dict:
        """getByProducsIDs

        Args:
            productID (list): Product IDs for the products to retrieve from the database. Enter up to 20 PIDs separated by commas. For example: 15216-OADM1-35=,M92S1K9-1.3.3C Note: To enhance search capabilities, the Cisco Support Tools allows wildcards with the productIDs parameter. A minimum of 3 characters is required. For example, only the following inputs are valid: *VPN*, *VPN, VPN*, and VPN. Using wildcards can result in multiple PIDs in the output.
            pageIndex (int, optional): Index number of the page to return; a maximum of 50 records per page are returned. Defaults to 1.

        Returns:
            dict: {PaginationResponseRecord, EOXRecord}
        """
        params = {
            'responseencoding': 'json'
        }

        productID = ','.join(productID)

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/{pageIndex}/{productID}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getBySerialNumbers(self,serialNumber: list , pageIndex: int = 1) -> dict:
        """getBySerialNumbers

        Args:
            serialNumber (list): Device serial number or numbers for which to return results. You can enter up to 20 serial numbers (each with a maximum length of 40) separated by commas.
            pageIndex (int, optional): Index number of the page to return; a maximum of 50 records per page are returned. Defaults to 1.

        Returns:
            dict: {PaginationResponseRecord, EOXRecord}
        """
        params = {
            'responseencoding': 'json'
        }

        serialNumber = ','.join(serialNumber)

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/{pageIndex}/{serialNumber}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()

    def getBySoftwareReleaseStrings(self, software: list , pageIndex:int = 1) -> dict:
        """getBySoftwareReleaseStrings

        Args:
            software (list): String for software release and type of operating system (optional) for the requested product. For example: 12.2,IOS You can enter up to 20 software release and operating system type combinations. Each combination can return multiple EoX records.
            pageIndex (int, optional): Index number of the page to return. For example, 1 returns the first page of the total number of available pages. Defaults to 1.

        Returns:
            dict: {PaginationResponseRecord, EOXRecord}
        """
        params = {
            'responseencoding': 'json'
        }

        for i, sw in enumerate(software):
            params.update({
                f'input{i+1}': sw
            })

        url = f'https://api.cisco.com/supporttools/eox/rest/5/EOXBySWReleaseString/{pageIndex}'
        r = requests.get(url=url, headers=self.__headers, params=params, verify=self.__verify, proxies=self.__proxies)

        return r.json()