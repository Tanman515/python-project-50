from gendiff.reader import read
from gendiff.parser import parse
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.to_json import make_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read(file_path1)
    data2 = read(file_path2)
    diff = parse(data1, data2)
    if format_name == 'plain':
        data = plain(diff)
    elif format_name == 'json':
        data = make_json(diff)
    else:
        data = stylish(diff)
    return data
