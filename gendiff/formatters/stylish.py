from gendiff.encode import encode


def form(diff):
    formatted = '{'
    indent = '  '
    for key in sorted(diff.keys()):
        same = encode(diff[key].get('same'))
        removed = encode(diff[key].get('removed'))
        added = encode(diff[key].get('added'))
        if 'same' in diff[key]:
            formatted += '\n{}  {}: {}'.format(indent, key, same)
        if 'removed' in diff[key]:
            formatted += '\n{}- {}: {}'.format(indent, key, removed)
        if 'added' in diff[key]:
            formatted += '\n{}+ {}: {}'.format(indent, key, added)
    return formatted + '\n}'
