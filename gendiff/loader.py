import json
import yaml


def load_(path):
    abs_path, ext = path
    with open(abs_path, 'r') as file_to_convert:
        if ext == 'json':
            loaded = json.load(file_to_convert)
        elif ext == 'yaml' or ext == 'yml':
            loaded = yaml.safe_load(file_to_convert)
        else:
            raise AttributeError
    return loaded
