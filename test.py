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

### EoX ###
# eox = EoX(client_key, client_secret)

# a = eox.getByDates('2021-01-01','2021-01-31')
# print(json.dumps(a, indent=4))

# b = eox.getByProducsIDs(['15216-OADM1-35=', 'M92S1K9-1.3.3C'])
# print(json.dumps(b, indent=4))

# c = eox.getBySerialNumbers(['FHK0933224R'])
# print(json.dumps(c, indent=4))

# d = eox.getBySoftwareReleaseStrings(['12.4(15)T,IOS', '12.4(14)T,IOS'])
# print(json.dumps(d, indent=4))

### Bug ###

bug = Bug(client_key, client_secret)

# a = bug.getByIDs(['CSCdr72939'])
# print(json.dumps(a, indent=4))

# b = bug.getByBaseProductIDs('WS-C3560-48PS-S', status='F', modified_date=5, severity=2, sort_by='modified_date')
# print(json.dumps(b, indent=4))

# c = bug.getByBaseProductIDsAndSoftwareReleases('WS-C3560-48PS-S', '12.2(25)SE', modified_date=5, sort_by='modified_date')
# print(json.dumps(c, indent=4))

# d = bug.getByKeywords(['cisco', 'firewall'])
# print(json.dumps(d, indent=4))

# e = bug.getByProductSeriesAndAffectedSoftwareRelease('Cisco 5500 Series Wireless Controllers', ['7.4(100.0)'])
# print(json.dumps(e, indent=4))

# f = bug.getByProductSeriesAndFixedInSoftwareRelease('Cisco Nexus 9000 Series Switches', ['10.1(1)'], modified_date=5)
# print(json.dumps(f, indent=4))

# g = bug.getByProductNameAndAffectedSoftwareRelease('Cisco Unity Connection Version 10.5', ['10.5(2)'], modified_date=5)
# print(json.dumps(g, indent=4))

# h = bug.getByProductNameAndFixedInSoftwareRelease('Cisco Unified Communications Manager (CallManager)', ['10.5'])
# print(json.dumps(h, indent=4))
