IND = '    '
MINUS = '  - '
PLUS = '  + '
SC = ': '


def form_view(diffs):
    lines = ['{']
    walk(diffs, lines, 0)
    return '\n'.join(lines)


def walk(diff, lines, lvl):
    lvl += 1
    indent = IND * (lvl - 1)
    for key, value in sorted(diff.items()):
        line = indent + IND + key + SC

        if isinstance(value, dict):
            same = value.get('same')
            added = value.get('added')
            removed = value.get('removed')

            if same:
                lines.append(line + same)

            if removed or removed in ['', 0, 'null']:
                minus = indent + MINUS + key + SC
                if isinstance(removed, dict):
                    lines.append(minus + '{')
                    walk(removed, lines, lvl)
                else:
                    lines.append(minus + str(removed))

            if added or added in ['', 0, 'null']:
                plus = indent + PLUS + key + SC
                if type(added) == dict:
                    lines.append(plus + '{')
                    walk(added, lines, lvl)
                else:
                    lines.append(plus + str(added))

            if added is None and removed is None and same is None:
                lines.append(line + '{')
                walk(value, lines, lvl)

        else:
            lines.append(line + str(value))

    lines.append(indent + '}')
