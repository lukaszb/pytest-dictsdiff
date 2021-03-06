import datetime
import decimal
import dictdiffer
import json
import pytest


@pytest.fixture
def dicts_are_same(pytestconfig):
    verbose = pytestconfig.getoption("verbose")

    def wrapper(d1, d2):
        return check_objects(d1, d2, verbose=verbose)

    return wrapper


def check_objects(d1, d2, verbose=0):
    if d1 == d2:
        return True
    else:
        diff_chunks = list(dictdiffer.diff(d1, d2))
        diff = "\n".join([diff_chunk_as_text(chunk) for chunk in diff_chunks])
        if verbose == 0:
            pytest.fail(diff)
        else:
            sep = "\n" + ("=" * 80) + "\n"
            msg_lines = [
                "Provided items are NOT the same.",
                "Left:",
                as_json(d1),
                sep,
                "Right:",
                as_json(d2),
                sep,
                "Diff:",
                diff,
            ]
            pytest.fail("\n\n".join(msg_lines))


def as_json(d):
    return json.dumps(d, sort_keys=True, indent=2, cls=JSONEncoder)


def diff_chunk_as_text(chunk):
    action, path, values = chunk
    text = " => %s: " % action.upper()

    if action == "change":
        text += "at key %r values are different | Left: %r | Right: %r" % (path, values[0], values[1])
    elif action == "add":
        text += "extra values under %r key on the right: %r" % (path, values)
    elif action == "remove":
        text += "missing values under %r key on the right: %r" % (path, values)

    return text


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, (datetime.datetime, datetime.date, datetime.time)):
            return o.isoformat()
        else:
            return super().default(o)
