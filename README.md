# Cisco Support APIs for Python

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/rothdennis/cisco_support)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/rothdennis/cisco_support/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rothdennis/cisco_support)](https://github.com/rothdennis/cisco_support/stargazers)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rothdennis/cisco_support)

Python implementation of the [Cisco Support API](https://developer.cisco.com/docs/support-apis/#!introduction-to-cisco-support-apis)

## Implemented APIs

- [ ] Automated Software Distribution
- [x] Bug
- [x] Case
- [x] EoX
- [x] Product Information
- [x] Serial Number to Information
- [x] Service Order Return (RMA)
- [x] Software Suggestion

## Installation

```bash
pip install cisco_support
```

## Usage

### Automated Software Distribution

> TO BE IMPLEMENTED

### Bug

```python
from cisco_support import Bug

bug = Bug(client_id='abc', client_secret='def')
```

### Case

```python
from cisco_support import Case

case = Case(client_id='abc', client_secret='def')
```

### EoX
```python
from cisco_support import EoX

eox = EoX(client_id='abc', client_secret='def')
```

### Product Information
```python
from cisco_support import ProductInformation

product_information = ProductInformation(client_id='abc', client_secret='def')
```

### Serial Number to Information
```python
from cisco_support import SerialNumberInformation

serial_number_information = SerialNumberInformation(client_id='abc', client_secret='def')
```

### Service Order Return (RMA)
```python
from cisco_support import ServiceOrderReturn

service_order_return = ServiceOrderReturn(client_id='abc', client_secret='def')
```

### Software Suggestion
```python
from cisco_support import SoftwareSuggestion

software_suggestion = SoftwareSuggestion(client_id='abc', client_secret='def')
```