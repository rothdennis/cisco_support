# Cisco Support APIs for Python 🐍

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/rothdennis/cisco_support)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/rothdennis/cisco_support/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rothdennis/cisco_support)](https://github.com/rothdennis/cisco_support/stargazers)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rothdennis/cisco_support)


Python implementation of the [Cisco Support API](https://developer.cisco.com/docs/support-apis/#!introduction-to-cisco-support-apis)

# What are the Cisco Support APIs?

The Cisco Support APIs remove barriers to enterprise automation and can help end users shorten sales cycles and reduce operating expenses. This new way of delivering support information empowers customers and partners to use Cisco data in new and innovative ways to increase productivity and add new value to their business. The beauty of this approach is in its flexibility. Specifically, the Support APIs leverage Cisco's strength in delivering rich knowledge while providing options to customers and partners as to how they want to consume it. In addition, the Cisco Support API foundation provides the reference for future customer-facing and partner-facing web services and applications that will enable customers and partners to more effectively support Cisco products, networks and applications within their own business processes and systems.

# Getting Started

## Overview
Cisco Support APIs are available only to Cisco Smart Net Total Care (SNTC) customers and Cisco Partner Support Service (PSS) partner. Access is gated by a role-based process that is administered by the customer or partner in the Cisco Services Access Manager tool. The remaining steps to gain access to the Cisco Support APIs depend on whether you are an SNTC customer or a PSS partner.

## Onboarding Process
To obtain access to the Cisco Support APIs you must assign someone from your organization as a Delegated Administrator. This individual is responsible for granting access to additional users and administrators within your organization. The process to onboard the Delegated Administrator depends on whether you are a Cisco Partner Service Support (PSS) partners or a Smart Net Total Care (SNTC) customer. Refer to the appropriate onboarding process here:

[Cisco API Console](https://apiconsole.cisco.com/)

## Install 

TBD
```
pip install cisco-support
```

## Use cisco_support

### Automated Software Distribution

> The Automated Software Distribution service provides software information and download URLs to assist you in upgrading your device/application to the latest version. You can find software images, verify MD5 checksum values, and electronically sign EULA and K9 agreements - all critical activities when upgrading.

TBD

```py
import json
from cisco_support import ASD

asd = ASD(client_key, client_secret)
```

### Bug

> The Bug API service provides access to Cisco defects (bugs) information. Customers and partners can request bug information for either specific bugs or lookup list of bugs at a product level. Bug API also allows lookup of bugs using keywords of interest.

```py
import json
from cisco_support import Bug

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

> The Case API service provides access to Cisco Support Case information. Using the Case API, customers and partners can request case information for either specific support cases or at an aggregate level (i.e. user, contract or customer level) using a variety of input parameters.

TBD
```py
import json
from cisco_support import Case

cases = Case(client_key, client_secret)
```

### EoX

> The End of Life (EoX) service provides access to Cisco EoX product data. Customers and partners can request Cisco EoX product information for both hardware and software using a variety of input parameters.

```py
import json
from cisco_support import EoX

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

> The Product Information API service provides access to Cisco product information associated with device serial numbers or product ids.

```py
import json
from cisco_support import PI

pi = PI(client_key, client_secret)

a = pi.getBySerialNumbers(['SPE181700LN','REF_CSJ07306405'])
print(json.dumps(a, indent=4))

b = pi.getByProductIDs(['UBR10012','ASR1001'])
print(json.dumps(b, indent=4))

c = pi.getMDFInformationByProductIDs(['ASA5505-50-BUN-K9'])
print(json.dumps(c, indent=4))
```

### Serial Number to Information

> The Serial Number to Information (SN2INFO) API service provides access to Cisco information associated with device serial numbers. Customers and partners can request orderable product identifier (PID), item description, warranty information and coverage status for set of serial numbers at a time.

```py
import json
from cisco_support import SNI

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

> The Service Order Return (RMA) API service provides access to Return Material Authorization (RMA) information. Customers and partners can request returns information for either specific returns or at an aggregate level (i.e. user level) using a variety of input parameters.

```py
import json
from cisco_support import RMA

rma = RMA(client_key, client_secret)

a = rma.getByRMANumber('84894022')
print(json.dumps(a, indent=4))

b = rma.getByUserID(['svorma8'])
print(json.dumps(b, indent=4))
```

### Software Suggestion

> The Software Suggestion API service provides access to Cisco suggested software based on stability, longevity, adoption rate and other factors for a growing list of Cisco products. Customers and partners can access Cisco suggested and other available software based on their product, feature upgrade needs and hardware configuration.

```py
import json
from cisco_support import SS

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
