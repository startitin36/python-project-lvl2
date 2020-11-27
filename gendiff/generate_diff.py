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
    old = json.load(open(file_path1))
    new = json.load(open(file_path2))
    for key in sorted((old.keys() | new.keys())):
        old_value = old.get(key)
        new_value = new.get(key)
        if old.get(key) == new_value:
            diff = '{0} {1}: {2}\n'.format('  ', key, old_value)
        elif not new_value:
            diff = '{0} {1}: {2}\n'.format(' -', key, old_value)
        elif not old_value:
            diff = '{0} {1}: {2}\n'.format(' +', key, new_value)
        else:
            diff = '{0} {1}: {2}\n{3} {4}: {5}\n'.format(' -', key, old_value, ' +', key, new_value)
        final += diff
    return '{0}'.format(final[:-1] + '\n}')
