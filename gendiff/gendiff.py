from gendiff import reader
from gendiff import to_json
from gendiff import parser


def generate_diff(file_path1, file_path2):
    data1 = reader.read(file_path1)
    data2 = reader.read(file_path2)
    diff = parser.parse(data1, data2)
    json = to_json.make_json(diff)
    return json
