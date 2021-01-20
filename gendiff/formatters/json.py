import json


def form_view(diff):
    return json.dumps(diff, indent=4)
