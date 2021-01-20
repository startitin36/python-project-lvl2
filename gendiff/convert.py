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
    if value == 0 and type(value) == int:
        return 0
    if value == 1 and type(value) == int:
        return 1
    if value in json_convert_list:
        return json.dumps(value)
    return value
