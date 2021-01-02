def form_view(diffs):
    lines = ['{']

    def walk(diff, indent):
        for key, value in diff.items():
            if key[0] not in ('+', '-', ' '):
                key = '  ' + key
            if isinstance(value, dict):
                lines.append(f'{indent}{key}: {{')
                walk(value, indent + '    ')
            else:
                if value == '' or value == "":
                    lines.append(f'{indent}{key}: ')
                else:
                    lines.append(f'{indent}{key}: {value}')
        lines.append(f'{indent[:-2]}}}')

    walk(transform(diffs), '  ')
    return '\n'.join(lines)


def transform(inner_tree):
    result = {}
    for key, value in sorted(inner_tree.items()):
        if isinstance(value, dict):
            same = value.get('same')
            added = value.get('added')
            removed = value.get('removed')
            if same:
                mod_key = '' + '' + key
                result[mod_key] = same
            if removed or removed == '':
                mod_key = '-' + ' ' + key
                result[mod_key] = removed
            if added or added == '':
                mod_key = '+' + ' ' + key
                result[mod_key] = added
            if added is None and removed is None and same is None:
                result[key] = transform(value)
        else:
            result[key] = value
    return result
