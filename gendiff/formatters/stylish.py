IND = '    '
MINUS = '  - '
PLUS = '  + '


def form_view(diffs):
    lines = ['{']
    walk(diffs, lines, 0)
    return '\n'.join(lines)


def walk(diff, lines, lvl):
    lvl += 1
    indent = IND * (lvl - 1)
    for key, value in sorted(diff.items()):
        if isinstance(value, dict):
            same = value.get('same')
            added = value.get('added')
            removed = value.get('removed')

            if same:
                lines.append(make_line(indent, key, IND, same))

            if removed or removed in ['', 0, 'null']:
                if isinstance(removed, dict):
                    lines.append(make_line(indent, key, MINUS, '{'))
                    walk(removed, lines, lvl)
                else:
                    lines.append(make_line(indent, key, MINUS, removed))

            if added or added in ['', 0, 'null']:
                if isinstance(added, dict):
                    lines.append(make_line(indent, key, PLUS, '{'))
                    walk(added, lines, lvl)
                else:
                    lines.append(make_line(indent, key, PLUS, added))

            if added is None and removed is None and same is None:
                lines.append(make_line(indent, key, IND, '{'))
                walk(value, lines, lvl)
        else:
            lines.append(make_line(indent, key, IND, value))
    lines.append(make_line(indent, '', '', ''))


def make_line(indent, key, change='', value=None):
    if key:
        return '{}{}{}: {}'.format(indent, change, key, value)
    else:
        return '{}{}{}'.format(indent, '', '}')
