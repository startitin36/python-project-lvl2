from gendiff.encode import encode
import json


def form_view(diff):
    # result = ['{']
    # for key in sorted(diff.keys()):
    #     result.append('{}: {}'.format(encode(key), diff[key]))
    # return json.dumps('\n'.join(result))
    return json.dumps(diff)
