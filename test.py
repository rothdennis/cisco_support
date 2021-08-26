from cisco_support.bug import Bug
from cisco_support.automated_software_distribution import ASD
from cisco_support.case import Case
from cisco_support.eox import EoX
from cisco_support.product_information import PI
from cisco_support.serial_number_information import SNI
from cisco_support.service_order_return import RMA
from cisco_support.software_suggestions import SS

import json
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

client_key = config['cisco_support']['client_key']
client_secret = config['cisco_support']['client_secret']

# Testing EoX
eox = EoX(client_key, client_secret)

a = eox.getByDates('2021-01-31','2021-03-31',1)
print(json.dumps(a, indent=4))

#eox.getByProducsIDs()
#eox.getBySerialNumbers()
#eox.getBySoftwareReleaseStrings()

# Testing ...
