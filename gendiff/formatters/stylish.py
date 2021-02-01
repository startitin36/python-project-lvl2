IND = '  '


def form_view(diffs):
    lines = ['{']

    def walk(diff, lvl):
        lvl += 1
        indent = IND * 2 * (lvl - 1)
        for key, value in sorted(diff.items()):
            if isinstance(value, dict):
                same = value.get('same')
                added = value.get('added')
                removed = value.get('removed')

                if same:
                    make_line(lines, indent, key,  IND * 2, same)

                if removed or removed in ['', 0, 'null']:
                    if isinstance(removed, dict):
                        make_line(lines, indent, key, '  - ', '{')
                        walk(removed, lvl)
                    else:
                        make_line(lines, indent, key, '  - ', removed)

                if added or added in ['', 0, 'null']:
                    if isinstance(added, dict):
                        make_line(lines, indent, key, '  + ', '{')
                        walk(added, lvl)
                    else:
                        make_line(lines, indent, key, '  + ', added)

                if added is None and removed is None and same is None:
                    make_line(lines, indent, key, IND * 2, '{')
                    walk(value, lvl)
            else:
                make_line(lines, indent, key, IND * 2, value)
        make_line(lines, indent, '', '', '')
    walk(diffs, 0)
    return '\n'.join(lines)


def make_line(lines, indent, key, change='', value=None):
    # sign = IND + signs.get(change)
    if key:
        lines.append('{}{}{}: {}'.format(indent, change, key, value))
    else:
        lines.append('{}{}{}'.format(indent, '', '}'))
