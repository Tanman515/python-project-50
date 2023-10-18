from gendiff import generate_diff


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()


def test_gendiff_plane():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == read_txt('tests/fixtures/expected_1.txt') #noqa
    assert generate_diff('tests/fixtures/file2.json', 'tests/fixtures/file3.json') == read_txt('tests/fixtures/expected_2.txt') #noqa
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.json') == read_txt('tests/fixtures/expected_3') #noqa
