from gendiff.gendiff.generate_diff import generate_diff
import json


file1 = 'file3.json'
file2 = 'file4.json'
#answer = '{\n- follow: False,\n  host: hexlet.io,\n- proxy: 123.234.53.22,\n- timeout: 50,\n+ timeout: 20,\n+ verbose: True\n}'
answer = open('./tests/split_answer.txt')

def test_split():
    assert generate_diff(file1, file2) == answer.read()
#'{\n- follow: False,\n  host: hexlet.io,\n- proxy: 123.234.53.22,\n- timeout: 50,\n+ timeout: 20,\n+ verbose: True\n}'
