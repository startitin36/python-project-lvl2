#!usr/bin/env python3

from gendiff.convert import convert
from gendiff.formatters import stylish
from gendiff.formatters import json
from gendiff.formatters import plain
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
    formatted_view = ''
    if form == 'stylish':
        formatted_view = stylish.form_view(diffs)
    if form == 'plain':
        formatted_view = plain.form_view(diffs)
    if form == 'json':
        formatted_view = json.form_view(diffs)
    return formatted_view


def find_diff(old, new):
    return dict(
        map(
            lambda x: (
                x, mark_state(
                    old.get(x), new.get(x),
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
    if before == after:
        return {'same': encode(before)}
    elif before is None:
        return {'added': encode(after)}
    elif after is None:
        return {'removed': encode(before)}
    elif before != after:
        if isinstance(after, dict) and isinstance(before, dict):
            return find_diff(before, after)
        return {'removed': encode(before), 'added': encode(after)}
