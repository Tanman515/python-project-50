from gendiff import generate_diff


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()


expected_1 = read_txt('C:/Users/User/gendiff/tests/fixtures/expected1.txt')
expected_2 = read_txt('C:/Users/User/gendiff/tests/fixtures/expected2.txt')
expected_3 = read_txt('C:/Users/User/gendiff/tests/fixtures/expected3.txt')


def test_gendiff_plane():
    assert generate_diff('C:/Users/User/gendiff/tests/fixtures/file1.json', 'C:/Users/User/gendiff/tests/fixtures/file2.json') == expected_1
    assert generate_diff('C:/Users/User/gendiff/tests/fixtures/file2.json', 'C:/Users/User/gendiff/tests/fixtures/file3.json') == expected_2
    assert generate_diff('C:/Users/User/gendiff/tests/fixtures/file1.json', 'C:/Users/User/gendiff/tests/fixtures/file3.json') == expected_3
