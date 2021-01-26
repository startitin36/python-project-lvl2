from gendiff.convert import convert


def find_diff(old, new):
    """Find diff between two dicts: before and after changes.

    Arguments:
        old (dict): dict before changes
        new (dict): dict after changes

    Returns:
        dict of/with changes.
    """
    all_keys = old.keys() | new.keys()
    diffs = map(lambda key: (
        key, mark_diff(get_value(old, key), get_value(new, key))), all_keys
    )

    return dict(diffs)


def mark_diff(before, after):
    """Mark changes of values of the same
    key in dicts before&after changes.

    Arguments:
        before: value of key in source dict,
        after: value of key in modified dict,

    Returns:
        one of three marks with value: 'added',
        'removed', 'same'.
        Example: {'key': {'mark': value}}
    """

    bef_enc = convert(before)
    aft_enc = convert(after)

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
        return convert(node.get(key))
    return None
