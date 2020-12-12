import json


json_encode_list = [
    dict,
    list,
    str,
    int,
    float,
    True,
    False,
    None
]


def encode(value):
    if value in json_encode_list:
        return json.dumps(value)
    return value
