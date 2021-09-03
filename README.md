# Cisco's Support APIs for Python

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/rothdennis/cisco_support) Not approved yet!

Implementation of the [Cisco Support API Docs](https://developer.cisco.com/docs/support-apis/#!introduction-to-cisco-support-apis)

[Cisco API Console](https://apiconsole.cisco.com/)

## How to

### Automated Software Distribution

TBD
```py
import json
from cisco_support.automated_software_distribution import ASD

asd = ASD(client_key, client_secret)
```

### Bug

```py
import json
from cisco_support.bug import Bug

bugs = Bug(client_key, client_secret)

a = bugs.getByIDs(['CSCdr72939'])
print(json.dumps(a, indent=4))

b = bugs.getByBaseProductIDs('WS-C3560-48PS-S', status='F', modified_date=5, severity=2, sort_by='modified_date')
print(json.dumps(b, indent=4))

c = bugs.getByBaseProductIDsAndSoftwareReleases('WS-C3560-48PS-S', '12.2(25)SE', modified_date=5, sort_by='modified_date')
print(json.dumps(c, indent=4))

d = bugs.getByKeywords(['cisco', 'firewall'])
print(json.dumps(d, indent=4))

e = bugs.getByProductSeriesAndAffectedSoftwareRelease('Cisco 5500 Series Wireless Controllers', ['7.4(100.0)'])
print(json.dumps(e, indent=4))

f = bugs.getByProductSeriesAndFixedInSoftwareRelease('Cisco Nexus 9000 Series Switches', ['10.1(1)'], modified_date=5)
print(json.dumps(f, indent=4))

g = bugs.getByProductNameAndAffectedSoftwareRelease('Cisco Unity Connection Version 10.5', ['10.5(2)'], modified_date=5)
print(json.dumps(g, indent=4))

h = bugs.getByProductNameAndFixedInSoftwareRelease('Cisco Unified Communications Manager (CallManager)', ['10.5'])
print(json.dumps(h, indent=4))

```

### Case

TBD
```py
import json
from cisco_support.case import Case

cases = Case(client_key, client_secret)
```

### EoX

```py
import json
from cisco_support.eox import EoX

eox = EoX(client_key, client_secret)

a = eox.getByDates('2021-01-01','2021-01-31')
print(json.dumps(a, indent=4))

b = eox.getByProducsIDs(['15216-OADM1-35=', 'M92S1K9-1.3.3C'])
print(json.dumps(b, indent=4))

c = eox.getBySerialNumbers(['FHK0933224R'])
print(json.dumps(c, indent=4))

d = eox.getBySoftwareReleaseStrings(['12.4(15)T,IOS', '12.4(14)T,IOS'])
print(json.dumps(d, indent=4))
```

### Product Information

```py
import json
from cisco_support.product_information import PI

pi = PI(client_key, client_secret)

a = pi.getBySerialNumbers(['SPE181700LN','REF_CSJ07306405'])
print(json.dumps(a, indent=4))

b = pi.getByProductIDs(['UBR10012','ASR1001'])
print(json.dumps(b, indent=4))

c = pi.getMDFInformationByProductIDs(['ASA5505-50-BUN-K9'])
print(json.dumps(c, indent=4))
```

### Serial Number to Information

```py
import json
from cisco_support.serial_number_information import SNI

nsi = SNI(client_key, client_secret)

a = nsi.getCoverageStatusBySerialNumbers(['FOC10220LK9'])
print(json.dumps(a, indent=4))

b = nsi.getCoverageSummaryByInstanceNumbers(['917280220'])
print(json.dumps(b, indent=4))

c = nsi.getCoverageSummaryBySerialNumbers(['SAL09232Q0Z','32964768','FOC0903N5J9','INM07501EC3','SWCAT1239A0CJ'])
print(json.dumps(c, indent=4))

d = nsi.getOrderableProductIDsBySerialNumbers(['FOC10220LK9'])
print(json.dumps(d, indent=4))

e = nsi.getOwnerCoverageStatusBySerialNumbers(['FOC0717W107','FOC11517LEX','FOC0737Y43K'])
print(json.dumps(e, indent=4))
```

### Service Order Return (RMA)

```py
import json
from cisco_support.service_order_return import RMA

rma = RMA(client_key, client_secret)

a = rma.getByRMANumber('84894022')
print(json.dumps(a, indent=4))

b = rma.getByUserID(['svorma8'])
print(json.dumps(b, indent=4))
```

### Software Suggestion

```py
import json
from cisco_support.software_suggestions import SS

ss = SS(client_key, client_secret)

a = ss.getSuggestedReleasesAndImagesByProductIDs(['ASR-903','CISCO2811','N7K-C7018'])
print(json.dumps(a, indent=4))

b = ss.getSuggestedReleasesByProductIDs(['ASR-903','N7KS1K9-404','CISCO2811', 'ONS-GX-2FC-MMI'])
print(json.dumps(b, indent=4))

c = ss.getCompatibleAndSuggestedSoftwareReleasesByProductID('ASR1013')
print(json.dumps(c, indent=4))

d = ss.getSuggestedReleasesAndImagesByMDFIDs(['283933147','283780951'])
print(json.dumps(d, indent=4))

e = ss.getSuggestedReleasesByMDFIDs(['283933147','283780951'])
print(json.dumps(e, indent=4))

f = ss.getCompatibleAndSuggestedSoftwareReleasesByMDFID('283795847')
print(json.dumps(f, indent=4))
```
