from gendiff.reader import read
from gendiff.parser import parse
from gendiff.formatter import stylish


def generate_diff(file_path1, file_path2, formatter=stylish):
    data1 = read(file_path1)
    data2 = read(file_path2)
    diff = parse(data1, data2)
    format = formatter(diff)
    return format
