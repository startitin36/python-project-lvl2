#!usr/bin/env python3
"""To pars arguments."""
import argparse

from gendiff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default='stylish', type=str,
                    choices=['plain', 'json', 'stylish'],
                    help='set format of output: "plain", "json" or'
                    ' "stylish"(by default)')
args = parser.parse_args()


def main():
    """Return difference of 2 json or yaml.

    Returns:
        str: difference between given 2 files.
    """
    print(
        generate_diff.generate_diff(
            args.first_file, args.second_file, args.format
        )
    )


if __name__ == '__main__':
    main()
