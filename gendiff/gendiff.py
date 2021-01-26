#!usr/bin/env python3

from gendiff.parser import parse
from gendiff.loader import load_
from gendiff.formatters.outputs import outputs
from gendiff.find_diff import find_diff


def generate_diff(path1, path2, form='stylish'):
    """Summary line.

    Description
    Take 2 paths to files with json or yaml dicts and form
    output('stylish' by default)
    shows differences between them in defined output style:
    plain, json, stylish(default).
    convert() returns 2 dicts.

    Arguments:
        path1 (str): path to file before changes
        path2 (str): after changes
        form (str): output

    Returns:
        diffs string in required output style.
    """
    old = load_(parse(path1))
    new = load_(parse(path2))

    diffs = find_diff(old, new)
    return outputs.get(form)(diffs)
