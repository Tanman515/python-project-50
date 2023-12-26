from gendiff.reader import read
from gendiff.parser import parse
from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.to_json import make_json


def get_view(data):
    data1 = data[0]
    data2 = data[1]
    result = {}
    for key, value in data2.items():
        if key not in data1:
            result[key] = ('added', value)

    for key, value in data1.items():
        if key not in data2.keys():
            result[key] = ('removed', value)
            continue

        if not isinstance(value, dict):
            if value == data2.get(key):
                result[key] = ('same', value)
            else:
                result[key] = ('changed', value, data2.get(key))
        else:
            if isinstance(data2.get(key), dict):
                result[key] = ('same', get_view((value, data2.get(key))))
            else:
                result[key] = ('changed', value, data2.get(key))
    return result


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read(file_path1)
    data2 = read(file_path2)
    if file_path1.split('.')[-1] == 'json':
        type = 'json'
    elif file_path1.split('.')[-1] in ('yaml', 'yml'):
        type = 'yaml'
    parsing = parse(data1, data2, type)
    diff = get_view(parsing)
    if format_name == 'plain':
        data = plain(diff)
    elif format_name == 'json':
        data = make_json(diff)
    else:
        data = make_stylish(diff)
    return data