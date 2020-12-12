#!usr/bin/env python3

from gendiff.convert import convert
from gendiff.formatters import stylish
from gendiff.formatters import json
from gendiff.formatters import plain

NO_VAL = 'no_value'


def generate_diff(file1, file2, form='stylish'):
    """Summary line.

    Description
    Take 2 paths to files with json or yaml dicts and form of
    output('stylish' by default)
    shows differences between them in defined output style:
    plain, json, stylish(default).
    convert() returns 2 dicts.

    Arguments:
        file1 (str): path to file before changes
        file2 (str): after changes
        form (str): style of result output

    Returns:
        diffs string in requires style
    """
    old, new = convert([file1, file2])
    diffs = dict(
        map(
            lambda x: (
                x, mark_state(
                    old.get(x, NO_VAL), new.get(x, NO_VAL),
                ),
            ), (old.keys() | new.keys()),
        ),
    )
    formatted_view = ''
    if form == 'stylish':
        formatted_view = stylish.form(diffs)
    if form == 'plain':
        formatted_view = plain.form(diffs)
    if form == 'json':
        formatted_view = json.form(diffs)
    return formatted_view


def mark_state(before, after):
    """Fix changes between 2 value.

    Arguments:
        before: value of key in source file,
        after: value of key in modified file,

    Returns:
        dict of changes
    """
    if before == after:
        state = {'same': before}
    elif before == NO_VAL:
        state = {'added': after}
    elif after == NO_VAL:
        state = {'removed': before}
    else:
        state = {'removed': before, 'added': after}
    return state
