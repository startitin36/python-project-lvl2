from gendiff.generate_diff import generate_diff
import json
import pytest


def test_split():
    file2 = './tests/fixtures/after.json'
    file1 = './tests/fixtures/before.json'
    #with open('./tests/fixtures/split_diff.txt', 'r') as answer:
        #expected = json.loads(answer.read())
    expected2 = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'
    result = generate_diff(file1, file2)
    assert result == expected2
