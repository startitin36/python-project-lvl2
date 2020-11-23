#!usr/bin/env python3

import argparse
import json


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f', '--format',
    type=str,
    help='set format of output'
)
args = parser.parse_args()


def generate_diff(file_path1, file_path2):
    result = ''
    difference = ''
    first_json = json.load(open(file_path1))
    second_json = json.load(open(file_path2))
    all_keys_sorted = sorted(first_json.keys() + second_json.keys())
    for key in all_keys_sorted:
        old_value = first_json.get(key)
        new_value = second_json.get(key)
        if old_value == new_value:
            difference = "{}, {}: {}\n".format("", key, old_value)
        if not new_value:
            difference = "{}, {}: {}\n".format("-", key, old_value)
        if not old_value:
            difference = "{}, {}: {}\n".format("+", key, new_value)
        else:
            difference = "{}, {}: {}\n{}, {}: {}\n".format("-", key, old_value, "+", key, new_value)
        result += difference
    return result


def main():
    pass


if __name__ == '__main__':
    main()
