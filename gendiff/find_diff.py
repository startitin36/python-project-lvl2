from gendiff.convert import convert

REM = 'removed'
ADD = 'added'
SAME = 'same'


def find_diff(old, new):
    diff = {}

    same_keys = old.keys() & new.keys()
    for key in same_keys:
        diff[key] = mark_diff(old[key], new[key])

    removed_keys = old.keys() - new.keys()
    for key in removed_keys:
        diff[key] = {REM: convert(old[key])}

    added_keys = new.keys() - old.keys()
    for key in added_keys:
        diff[key] = {ADD: convert(new[key])}

    return diff


def mark_diff(old, new):
    old_value = convert(old)
    new_value = convert(new)
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return find_diff(old_value, new_value)
    if old_value == new_value:
        return {SAME: old_value}
    return {REM: old_value, ADD: new_value}


def get_value(node, key):
    if key in node:
        return convert(node.get(key))
    return None
