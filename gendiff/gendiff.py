#!usr/bin/env python3
"""Takes 2 paths to json or yaml files  and
   shows differences between them in defined output style:
   plain, json, stylish(default)
   """
from gendiff.convert import convert
from gendiff.formatters import stylish
from gendiff.formatters import json
from gendiff.formatters import plain


def generate_diff(file1, file2, form='stylish'):
    """Take 2 paths to files with json or yaml dicts and form of
    output('stylish' by default)
    shows differences between them in defined output style:
     plain, json, stylish(default). c
     convert() returns 2 dicts.

    Arguments:
        file1 (str): path to file before changes
        file2 (str): after changes
        form (str): style of result output
    """
    old, new = convert([file1, file2])
    """mark_state(key_value_before, key_value_after) takes values of key before and 
    after, marks diffs between them.
    """
    def mark_state(before, after):
        if before == after:
            state = {'same': before}
        elif before == 'no_value':
            state = {'added': after}
        elif after == 'no_value':
            state = {'removed': before}
        else:
            state = {'removed': before, 'added': after}
        return state
    diffs = dict(map(lambda x: (x, mark_state(
        old.get(x, 'no_value'), new.get(x, 'no_value'))), (old.keys() | new.keys())))
    formatted_view = ''
    if form == 'stylish':
        formatted_view = stylish.form(diffs)
    if form == 'plain':
        formatted_view = plain.form(diffs)
    if form == 'json':
        formatted_view = json.form(diffs)
    return formatted_view
