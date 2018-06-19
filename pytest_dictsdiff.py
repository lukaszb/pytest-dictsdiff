import dictdiffer
import json
import pytest


@pytest.fixture
def dicts_are_same(pytestconfig):

    def check_objects(d1, d2):
        verbose = pytestconfig.getoption('verbose')
        if d1 == d2:
            return True
        else:
            diff_chunks = list(dictdiffer.diff(d1, d2))
            diff = '\n'.join([diff_chunk_as_text(chunk) for chunk in diff_chunks])
            if verbose == 0:
                pytest.fail(diff)
            else:
                sep = '\n' + ('=' * 80) + '\n'
                msg_lines = [
                    'Provided items are NOT the same.',
                    'Left:',
                    as_json(d1),
                    sep,
                    'Right:',
                    as_json(d2),
                    sep,
                    'Diff:',
                    diff,
                ]
                pytest.fail('\n\n'.join(msg_lines))

    return check_objects


def as_json(d):
    return json.dumps(d, sort_keys=True, indent=2)


def diff_chunk_as_text(chunk):
    action, path, values = chunk
    text = ' => %s: ' % action.upper()

    if action == 'change':
        text += 'at key %r values are different | Left: %r | Right: %r' % (path, values[0], values[1])
    elif action == 'add':
        text += 'extra values under %r key on the right: %r' % (path, values)
    elif action == 'remove':
        text += 'missing values under %r key on the right: %r' % (path, values)

    return text
