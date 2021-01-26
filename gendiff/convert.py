import json


json_convert_list = [
    dict,
    list,
    str,
    int,
    float,
    True,
    False,
    None,
]


def convert(value):
    if value in [0, 1] and type(value) == int:
        return value
    if value in json_convert_list:
        return json.dumps(value)
    return value
