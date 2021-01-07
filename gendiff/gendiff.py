#!usr/bin/env python3

from gendiff.convert import convert
from gendiff.formatters import stylish
from gendiff.formatters import json
from gendiff.formatters import plain
from gendiff.formatters.forms import forms
from gendiff.encode import encode

NO_VAL = 'no_value'


def generate_diff(path1, path2, form='stylish'):
    """Summary line.

    Description
    Take 2 paths to files with json or yaml dicts and form of
    output('stylish' by default)
    shows differences between them in defined output style:
    plain, json, stylish(default).
    convert() returns 2 dicts.

    Arguments:
        path1 (str): path to file before changes
        path2 (str): after changes
        form (str): style of result output

    Returns:
        diffs string in required style.
    """
    old, new = convert([path1, path2])
    diffs = find_diff(old, new)
    return forms.get(form)(diffs)


def find_diff(old, new):
    return dict(
        map(
            lambda x: (
                x, mark_state(
                    get_value(old, x), get_value(new, x),
                ),
            ), (old.keys() | new.keys()),
        ),
    )


def mark_state(before, after):
    """Fix changes between 2 value.

    Arguments:
        before: value of key in source file,
        after: value of key in modified file,

    Returns:
        dict of changes
    """

    bef_enc = encode(before)
    aft_enc = encode(after)
    if bef_enc == aft_enc:
        return {'same': bef_enc}
    elif before is None and type(before) != str:
        return {'added': aft_enc}
    elif after is None and type(after) != str:
        return {'removed': bef_enc}
    elif bef_enc != aft_enc:
        if isinstance(after, dict) and isinstance(before, dict):
            return find_diff(before, after)
        return {'removed': bef_enc, 'added': aft_enc}


def get_value(node, key):
    if key in node:
        return encode(node.get(key))
    return None
