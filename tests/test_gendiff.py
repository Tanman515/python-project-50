from gendiff import generate_diff


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()


schema = 'tests/fixtures/'


def test_json():
    assert generate_diff(f'{schema}file1.json', f'{schema}file2.json') == read_txt(f'{schema}expected1.txt')


def test_yaml():
    assert generate_diff(f'{schema}file1.yaml', f'{schema}file2.yaml') == read_txt(f'{schema}expected1.txt')


def test_with_inner_json():
    assert generate_diff(f'{schema}file1_inner.json', f'{schema}file2_inner.json') == read_txt(f'{schema}expected2.txt')


def test_with_inner_yaml():
    assert generate_diff(f'{schema}file1_inner.yaml', f'{schema}file2_inner.yaml') == read_txt(f'{schema}expected2.txt')


def test_json_plain():
    assert generate_diff(f'{schema}file1.json', f'{schema}file2.json', 'plain') == read_txt(f'{schema}expected3.txt')


def test_yaml_plain():
    assert generate_diff(f'{schema}file1.yaml', f'{schema}file2.yaml', 'plain') == read_txt(f'{schema}expected3.txt')


def test_with_inner_json_plain():
    assert generate_diff(f'{schema}file1_inner.json', f'{schema}file2_inner.json', 'plain') == read_txt(f'{schema}expected4.txt')


def test_with_inner_yaml_plain():
    assert generate_diff(f'{schema}file1_inner.yaml', f'{schema}file2_inner.yaml', 'plain') == read_txt(f'{schema}expected4.txt')


def test_json_style():
    assert generate_diff(f'{schema}file1_inner.json', f'{schema}file2_inner.json', 'json') == read_txt(f'{schema}expected5.txt')