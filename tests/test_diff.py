from gendiff import gendiff
from json import loads


def test_split_json():
    file2 = './tests/fixtures/after.json'
    file1 = './tests/fixtures/before.json'
    with open('./tests/fixtures/split_diff.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected


def test_split_yaml():
    file2 = './tests/fixtures/after.yaml'
    file1 = './tests/fixtures/before.yaml'
    with open('./tests/fixtures/split_diff.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected


def test_complex_json_stylish():
    file2 = './tests/fixtures/complex_2.json'
    file1 = './tests/fixtures/complex_1.json'
    with open('./tests/fixtures/complex_stylish.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected


def test_complex_yaml_stylish():
    file2 = './tests/fixtures/complex_2.yaml'
    file1 = './tests/fixtures/complex_1.yaml'
    with open('./tests/fixtures/complex_stylish.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected


def test_complex_json_plain():
    file2 = './tests/fixtures/complex_2.json'
    file1 = './tests/fixtures/complex_1.json'
    with open('./tests/fixtures/complex_plain.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2, 'plain')
    assert result == expected


def test_0_plain():
    file2 = './tests/fixtures/test_01.json'
    file1 = './tests/fixtures/test_00.json'
    with open('./tests/fixtures/test_plain.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2, 'plain')
    assert result == expected


def test_complex_yaml_json():
    file2 = './tests/fixtures/complex_2.yaml'
    file1 = './tests/fixtures/complex_1.yaml'
    # expected = loads('./tests/fixtures/json.json').read()
    with open('./tests/fixtures/json.json') as answer:
        expected = loads(answer.read())
    result = loads(gendiff.generate_diff(file1, file2, 'json'))
    assert result == expected


def test_complex_json_json():
    file2 = './tests/fixtures/complex_2.json'
    file1 = './tests/fixtures/complex_1.json'
    # expected = loads('./tests/fixtures/json.json').read()
    with open('./tests/fixtures/json.json') as answer:
        expected = loads(answer.read())
    result = loads(gendiff.generate_diff(file1, file2, 'json'))
    assert result == expected
