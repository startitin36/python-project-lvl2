def form_view(diff):
    view_lines = ['{']

    def walk(sub_tree, indent):
        for key, value in sub_tree.items():
            if key[0] not in ('+', '-', ' '):
                key = '  ' + key
            if isinstance(value, dict):
                view_lines.append(f'{indent}{key}: {{')
                walk(value, indent + '    ')
            else:
                view_lines.append(f'{indent}{key}: {value}')
        view_lines.append(f'{indent[:-2]}}}')

    walk(transform(diff), '  ')
    return '\n'.join(view_lines)


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
            if removed:
                mod_key = '-' + ' ' + key
                result[mod_key] = removed
            if added:
                mod_key = '+' + ' ' + key
                result[mod_key] = added
            if added is None and removed is None and same is None:
                result[key] = transform(value)
        else:
            result[key] = value
    return result
