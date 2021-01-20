from os.path import abspath, splitext


def parse(path):
    abs_path, ext = abspath(path), splitext(path)[1][1:]
    return abs_path, ext
