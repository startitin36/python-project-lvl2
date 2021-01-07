simples = (bool, int, float, str)
COMPLEX_VAL = '[complex value]'
code_list = [
    'false',
    'true',
    'null',
]
PROP = 'Property \'{}\' was '
UPD = PROP + 'updated. From {} to {}'
ADD = PROP + 'added with value: {}'
REM = PROP + 'removed'


def form_view(diffs):
    lines = []

    def walk(diff, path):
        for key, value in sorted(diff.items()):
            if isinstance(value, dict):
                val_bef, val_aft = value.get('removed'), value.get('added')
                if 'same' in value:
                    continue
                elif (val_bef or val_bef == '' or val_bef == 0) and (
                    val_aft or val_aft == '' or val_aft == 'null' or
                    val_aft == 0
                ):
                    val_bef, val_aft = def_value(val_bef), def_value(val_aft)
                    lines.append(
                        UPD.format(make_path(path, key), val_bef, val_aft)
                    )
                elif val_bef and 'added' not in value:
                    lines.append(REM.format(make_path(path, key)))
                elif val_aft and 'removed' not in value:
                    val_aft = def_value(val_aft)
                    lines.append(ADD.format(make_path(path, key), val_aft))
                else:
                    walk(value, make_path(path, key))

    walk(diffs, '')
    return '\n'.join(lines)


def def_value(value):
    if type(value) in simples:
        # if value == '':
        #     return ''
        if value == 0:
            return f'{0}'
        if value in code_list:
            return value
        return f'\'{value}\''
    return COMPLEX_VAL


def make_path(paths, key):
    if paths == '':
        return key
    return paths + '.' + key
