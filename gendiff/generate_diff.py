#!usr/bin/env python3
"""To open json."""
import json


def generate_diff(file_path1, file_path2):
    """Feel in with paths to 2 files json or yaml.

    Arguments:
        file_path1 (str): path to the first file
        file_path2 (str): path to the second file

    Returns:
        str: difference between given 2 files.
    """
    final = '{\n'
    with open(file_path1, 'r') as before:
        old = json.load(before)
    with open(file_path2, 'r') as after:
        new = json.load(after)
    for key in sorted((old.keys() | new.keys())):
        if old.get(key) == new.get(key):
            diff = '{0} {1}: {2}\n'.format('  ', key, old.get(key))
        elif not new.get(key):
            diff = '{0} {1}: {2}\n'.format(' -', key, old.get(key))
        elif not old.get(key):
            diff = '{0} {1}: {2}\n'.format(' +', key, new.get(key))
        else:
            diff = '{0} {1}: {2}\n{3} {4}: {5}\n'.format(
                ' -', key, old.get(key), ' +', key, new.get(key),
            )
        final += diff
    return '{0}'.format(final[:-1] + '\n}')
