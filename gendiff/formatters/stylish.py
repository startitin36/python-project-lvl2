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
        line1 = indent + IND + key + SC

        if isinstance(value, dict):
            same = value.get('same')
            added = value.get('added')
            removed = value.get('removed')

            if same:
                lines.append(line1 + same)

            if removed or removed in ['', 0, 'null']:
                minus = indent + MINUS + key + SC
                if isinstance(removed, dict):
                    lines.append(minus + '{')
                    walk(removed, lines, lvl)
                else:
                    lines.append(minus + str(removed))

            if added or added in ['', 0, 'null']:
                line = indent + PLUS + key + SC
                if isinstance(added, dict):
                    lines.append(line + '{')
                    walk(added, lines, lvl)
                else:
                    lines.append(line + str(added))

            if added is None and removed is None and same is None:
                lines.append(line1 + '{')
                walk(value, lines, lvl)
        else:
            lines.append(line1 + str(value))
    lines.append(indent + '}')
