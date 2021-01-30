IND = '  '
signs = {
    'same': IND,
    'added': '+ ',
    'removed': '- ',
    'empty': '',
}


def form_view(diffs):
    lines = ['{']

    def walk(diff, lvl):
        lvl += 1
        indent = IND * 2 * (lvl - 1)
        for key, value in sorted(diff.items()):
            if isinstance(value, dict):
                same = value.get('same')
                added = value.get('added')
                remd = value.get('removed')

                if same:
                    if isinstance(same, dict):
                        make_line(lines, indent, key, 'same')
                        walk(same, lvl)
                    else:
                        make_line(lines, indent, key,  'same', same)

                if remd or remd == '' or remd == 0 or remd == 'null':
                    if isinstance(remd, dict):
                        make_line(lines, indent, key, 'removed')
                        walk(remd, lvl)
                        # make_line(lines, indent, '', 'same')
                    else:
                        make_line(lines, indent, key, 'removed', remd)

                if added or added == '' or added == 0 or added == 'null':
                    if isinstance(added, dict):
                        make_line(lines, indent, key, 'added')
                        walk(added, lvl)
                        # make_line(lines, indent, '', 'same')
                    else:
                        make_line(lines, indent, key, 'added', added)

                if added is None and remd is None and same is None:
                    make_line(lines, indent, key, 'same')
                    walk(value, lvl)
            else:
                make_line(lines, indent, key, 'same', value)
        make_line(lines, indent, '', 'empty')
    walk(diffs, 0)
    return '\n'.join(lines)


def make_line(lines, indent, key, change='empty', value='{'):
    sign = IND + signs[change]
    if key:
        lines.append('{}{}{}: {}'.format(indent, sign, key, value))
    else:
        lines.append('{}{}{}'.format(indent, '', '}'))
