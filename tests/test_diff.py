from gendiff.generate_diff import generate_diff
import json
import pytest



def test_split_json_1():
    print('***1. The string is right in the test***')
    file2 = './tests/fixtures/after.json'
    file1 = './tests/fixtures/before.json'
    expected2 = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'
    result = generate_diff(file1, file2)
    assert result == expected2
    


def test_split_json_2():
    print('***2. The string and diff are loaded with json.loads***')
    file2 = './tests/fixtures/after.json'
    file1 = './tests/fixtures/before.json'
    with open('./tests/fixtures/split_diff.txt', 'r') as answer:
        expected = json.loads(answer)
    result = generate_diff(file1, file2)
    assert json.loads(result) == expected    
    
def test_split_json_3():
    print('***3. The string(formatted) and diff are loaded with json.loads***')
    file2 = './tests/fixtures/after.json'
    file1 = './tests/fixtures/before.json'
    with open('./tests/fixtures/split.json', 'r') as answer:
        expected = json.loads(answer.read())
    result = generate_diff(file1, file2)
    assert json.loads(result) == expected  
   

