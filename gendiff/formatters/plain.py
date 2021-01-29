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


def form_view(diff):
    """Take diff of two dicts and form 'plain' view.

    Arguments:
        diff (dict): dict with marked changes between two dicts

    Returns:
        string in 'plain' format
    """
    # create list to accumulate output view lines
    output = []

    # look for changes though all dict
    walk(diff, '', output)
    return '\n'.join(output)


def walk(node, path, lines):
    """Walk throw node to find changed keys ('removed' and 'added') to append
    output lines.

    Arguments:
        node (dict): node to search changes in
        path (str): accumulates keys to change value
        lines (list): accumulates lines to output
    """
    for key, value in sorted(node.items()):
        # path = make_path(path, key)
        # look for changes keys in values to process them.
        # check if key's value type is dict to handle 'get' method
        if isinstance(value, dict):

            # get values of changes if they are present:
            val_bef, val_aft = value.get('removed'), value.get('added')

            #  no need 'same' key for 'plain' format
            if 'same' in value:
                continue

            # if there are both values: before and after changes:
            elif val_aft is not None and val_bef is not None:

                # mode value if it complex:
                val_bef, val_aft = mod_value(val_bef), mod_value(val_aft)

                # adding 'updated' line to preparing view:
                lines.append(
                    UPD.format(make_path(path, key), val_bef, val_aft)
                )

            # if value before presents and added does not:
            elif val_bef and 'added' not in value:

                # adding 'removed' line to preparing view:
                lines.append(REM.format(make_path(path, key)))

            # if value after presents and removed does not:
            elif val_aft and 'removed' not in value:
                val_aft = mod_value(val_aft)

                # adding 'added' line to preparing view:
                lines.append(ADD.format(make_path(path, key), val_aft))

            # if there is no changed keys in values:
            else:

                # push value as  key, add key to path and try walk() again:
                walk(value, make_path(path, key), lines)


def mod_value(value):
    """ Mod value for output view.

    Arguments:
        value (any): value to mod

    Returns:
        value (str): If value is not in (bool, int, float, str)
     returns [complex value], else 'value'
    """
    if type(value) in simples:
        if value == 0:
            return f'{value}'
        if value in code_list:
            return f'{value}'
        return f'\'{value}\''
    return COMPLEX_VAL


def make_path(paths, key):
    if paths == '':
        return key
    return paths + '.' + key
