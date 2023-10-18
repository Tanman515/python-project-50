from gendiff import generate_diff


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()

schema = 'tests/fixtures/'


def test_gendiff_plane():
    assert generate_diff(f'{schema}file1.json', f'{schema}file2.json') == read_txt(f'{schema}expected1.txt')
    assert generate_diff(f'{schema}file2.json', f'{schema}file3.json') == read_txt(f'{schema}expected2.txt')
    assert generate_diff(f'{schema}file1.json', f'{schema}file3.json') == read_txt(f'{schema}expected3.txt')
