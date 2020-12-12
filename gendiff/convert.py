from os.path import abspath, splitext
import json
import yaml


def convert(*args):
    def inner(path):
        abs_path, ext = abspath(path), splitext(path)[1][1:]
        with open(abs_path, 'r') as file_to_convert:
            if ext == 'json':
                converted = json.load(file_to_convert)
            elif ext == 'yaml' or 'yml':
                converted = yaml.safe_load(file_to_convert)
            else:
                raise AttributeError
        return converted
    return list(map(lambda x: inner(x), *args))
