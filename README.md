# cisco_support
Implementation of the Cisco Support API

## How to

### Automated Software Distribution

TBD
```py
from cisco_support.automated_software_distribution import ASD

asd = ASD(client_key, client_secret)
```

### Bug

TBD
```py
from cisco_support.bug import Bug

bugs = Bug(client_key, client_secret)
```

### Case

TBD
```py
from cisco_support.case import Case

cases = Case(client_key, client_secret)
```

### EoX

```py
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

TBD
```py
from cisco_support.product_information import PI

pi = PI(client_key, client_secret)
```

### Serial Number to Information

TBD
```py
from cisco_support.serial_number_information import SNI

sni = SNI(client_key, client_secret)
```

### Service Order Return (RMA)

TBD
```py
from cisco_support.service_order_return import RMA

rma = RMA(client_key, client_secret)
```

### Software Suggestion

TBD
```py
from cisco_support.software_suggestions import SS

ss = SS(client_key, client_secret)
```

## Links

[Cisco Support API Docs](https://developer.cisco.com/docs/support-apis/#!introduction-to-cisco-support-apis)
