from datetime import datetime, time, date
from decimal import Decimal as d

def test_dicts(dicts_are_same):
    dict1 = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}
    dict2 = {'a': 100, 'f': 2, 'c': {'d': 400, 'g': 5}}
    assert dicts_are_same(dict1, dict2)


def test_decimals(dicts_are_same):
  obj1 = {'d': d('1.1')}
  obj2 = {'d': d('1.2')}
  assert dicts_are_same(obj1, obj2)


def test_datetimes(dicts_are_same):
  obj1 = {'d': datetime(2018, 5, 3, 12, 15)}
  obj2 = {'d': datetime(2018, 5, 3, 12, 50)}
  assert dicts_are_same(obj1, obj2)


def test_times(dicts_are_same):
  obj1 = {'d': time(12, 15)}
  obj2 = {'d': time(12, 50)}
  assert dicts_are_same(obj1, obj2)


def test_dates(dicts_are_same):
  obj1 = {'d': date(2018, 5, 3)}
  obj2 = {'d': date(2018, 5, 4)}
  assert dicts_are_same(obj1, obj2)
