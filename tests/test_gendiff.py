from gendiff import generate_diff


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()


schema = 'tests/fixtures/'


def test_gendiff_json():
    assert generate_diff(f'{schema}file1.json', f'{schema}file2.json') == read_txt(f'{schema}expected1.txt')


def test_gendiff_yaml():
    assert generate_diff(f'{schema}file1.yaml', f'{schema}file2.yaml') == read_txt(f'{schema}expected1.txt')


def test_gendiff_with_inner_json():
    assert generate_diff(f'{schema}file1_inner.json', f'{schema}file2_inner.json') == read_txt(f'{schema}expected4.txt')


def test_gendiff_with_inner_yaml():
    assert generate_diff(f'{schema}file1_inner.yaml', f'{schema}file2_inner.yaml') == read_txt(f'{schema}expected4.txt')


