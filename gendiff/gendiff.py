from gendiff.reader import read
from gendiff.parser import parse
from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.to_json import make_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read(file_path1)
    data2 = read(file_path2)
    if file_path1.split('.')[-1] == 'json':
        type = 'json'
    elif file_path1.split('.')[-1] in ('yaml', 'yml'):
        type = 'yaml'
    diff = parse(data1, data2, type)
    if format_name == 'plain':
        data = plain(diff)
    elif format_name == 'json':
        data = make_json(diff)
    else:
        data = make_stylish(diff)
    return data
