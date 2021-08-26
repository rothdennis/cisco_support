# cisco_support
Implementation of the Cisco Support API

## How to

### Automated Software Distribution

TBD

### Bug

TBD

### Case

TBD

### EoX

```py
from cisco_support.eox import EoX

eox = EoX(client_key, client_secret)

eox.getByDates('2021-01-31','2021-03-31')

eox.getByProducsIDs(['15216-OADM1-35=', 'M92S1K9-1.3.3C'])

eox.getBySerialNumbers(['FHK0933224R'])

eox.getBySoftwareReleaseStrings(['12.4(15)T,IOS', '12.4(14)T,IOS'])

```

### Product Information

TBD

### Serial Number to Information

TBD

### Service Order Return (RMA)

TBD

### Software Suggestion

TBD

## Links

[Cisco Support API Docs](https://developer.cisco.com/docs/support-apis/#!introduction-to-cisco-support-apis)
