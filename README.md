# pytest-dictsdiff


## Installation

    $ pip install pytest-dictsdiff

## Usage


At your test use `dicts_are_same` fixture and use it to compare two
objects:

```python

def test_dicts(dicts_are_same):
    dict1 = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}
    dict2 = {'a': 100, 'f': 2, 'c': {'d': 400, 'g': 5}}
    assert dicts_are_same(dict1, dict2)

## Todos

- [ ] Use `pprint` instead of `json` when showing objects (currently it would fail
  if data would contain any non-json-serializable objects)


## Example

Save following snippet as `dicts.py` and run `pytest dicts.py`.

```python
from collections import OrderedDict


RESULT = OrderedDict({
    "cell": "(056)-022-8631",
    "dob": {
        "age": 44,
        "date": "1983-11-04T01:21:14Z"
    },
    "email": "zeyneb.elfring@example.com",
    "gender": "female",
    "id": {
        "name": "BSN",
        "value": "36180866"
    },
    "location": {
        "city": "tholen",
        "coordinates": {
            "latitude": "46.8823",
            "longitude": "175.8856"
        },
        "postcode": 64504,
        "state": "groningen",
        "street": "2074 adriaen van ostadelaan",
        "timezone": {
            "description": "Adelaide, Darwin",
            "offset": "+9:30"
        }
    },
    "login": {
        "md5": "bafe8cf9d37806a7b13edc218d5ff762",
        "password": "ontario",
        "salt": "QVBKgEjy",
        "sha1": "cacef09ff61072d1c55732963766fa84e919aa7a",
        "sha256": "cc86af47aedbdbb1de73ff10484996fe9785c47c0fc191b7c67eaf71e0782300",
        "username": "smallgorilla897",
        "uuid": "37e30c59-bc79-4172-aac6-e2c640e165fa"
    },
    "name": {
        "first": "zeyneb",
        "last": "elfring",
        "title": "mrs"
    },
    "nat": "NL",
    "phone": "(209)-143-9697",
    "picture": {
        "large": "https://randomuser.me/api/portraits/women/37.jpg",
        "medium": "https://randomuser.me/api/portraits/med/women/37.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/37.jpg"
    },
    "registered": {
        "age": 3,
        "date": "2014-12-07T06:54:14Z"
    }
})

EXPECTED_DATA = {
    "cell": "(056)-022-8631",
    "dob": {
        "age": 34,
        "date": "1953-11-04T01:21:04Z"
    },
    "email": "zeyneb.elfring@example.com",
    "gender": "female",
    "id": {
        "name": "BSN",
        "value": "36180866"
    },
    "location": {
        "city": "Tholen",
        "coordinates": {
            "latitude": "46.8823",
            "longitude": "175.8856"
        },
        "postcode": 64509,
        "state": "groningen",
        "street": "2074 adriaen van ostadelaan",
        "timezone": {
            "description": "Adelaide, Darwin",
            "offset": "+9:30"
        }
    },
    "login": {
        "md5": "bafe8cf9d37806a7b13edc218d5ff762",
        "password": "ontario",
        "salt": "QVBKgEjy",
        "sha1": "cacef09ff61072d1c55732963766fa84e919aa7a",
        "sha256": "cc86af47aedbdbb1de73ff10484996fe9785c47c0fc191b7c67eaf71e0782300",
        "username": "smallgorilla897",
        "uuid": "37e30c59-bc79-4172-aac6-e2c640e165fa"
    },
    "name": {
        "first": "Zeyneb",
        "last": "Elfring",
        "title": "mrs"
    },
    "nat": "NL",
    "phone": "(209)-143-9697",
    "picture": {
        "large": "https://randomuser.me/api/portraits/women/37.jpg",
        "medium": "https://randomuser.me/api/portraits/med/women/37.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/37.jpg"
    },
    "registered": {
        "age": 3,
        "date": "2014-12-07T06:54:14Z"
    }
}


def test_compare_dicts(dicts_are_same):
    assert dicts_are_same(RESULT, EXPECTED_DATA)

```
