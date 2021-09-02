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

# bug = Bug(client_key, client_secret)

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

### Automated Software Distribution ###

# asd = ASD(client_key, client_secret)

# a = asd.getByProductIDAndRelease(pid='ASR10012XOC3POS-RF', currentReleaseVersion='5.4.3')
# print(json.dumps(a, indent=4))

### Case ###

# cases = Case(client_key, client_secret)

#a = cases.getCaseSummary(case_ids=['682299374'], sort_by='STATUS')

#b = cases.getCaseDetails(['682299374'])

# c = cases.getByUserID(user_ids=['directcust4'], )

#d = cases.getByContractID(contract_ids=['1234567'], date_created_from='2017-04-01T00:00:00Z', date_created_to='2017-04-30T23:59:59Z')

### Product Information ###

# pi = PI(client_key, client_secret)

# a = pi.getBySerialNumbers(['SPE181700LN','REF_CSJ07306405'])
# print(json.dumps(a, indent=4))

# b = pi.getByProductIDs(['UBR10012','ASR1001'])
# print(json.dumps(b, indent=4))

# c = pi.getMDFInformationByProductIDs(['ASA5505-50-BUN-K9'])
# print(json.dumps(c, indent=4))

### Serial Number Information ###

# nsi = SNI(client_key, client_secret)

# a = nsi.getCoverageStatusBySerialNumbers(['FOC10220LK9'])
# print(json.dumps(a, indent=4))

# b = nsi.getCoverageSummaryByInstanceNumbers(['917280220'])
# print(json.dumps(b, indent=4))

# c = nsi.getCoverageSummaryBySerialNumbers(['SAL09232Q0Z','32964768','FOC0903N5J9','INM07501EC3','SWCAT1239A0CJ'])
# print(json.dumps(c, indent=4))

# d = nsi.getOrderableProductIDsBySerialNumbers(['FOC10220LK9'])
# print(json.dumps(d, indent=4))

# e = nsi.getOwnerCoverageStatusBySerialNumbers(['FOC0717W107','FOC11517LEX','FOC0737Y43K'])
# print(json.dumps(e, indent=4))

### Service Order Return (RMA) ###

# rma = RMA(client_key, client_secret)

# a = rma.getByRMANumber('84894022')
# print(json.dumps(a, indent=4))

# b = rma.getByUserID(['svorma8'])
# print(json.dumps(b, indent=4))