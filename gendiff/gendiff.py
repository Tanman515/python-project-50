import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def find_diff(path1, path2):
    data1 = read_json(path1)
    data2 = read_json(path2)
    diff = {}
    for key, value in data1.items():
        if value == data2.get(key) and key in data2.keys():
            key = '  ' + key
            diff[key] = value
        elif value != data2.get(key) and key in data2.keys():
            key1 = '- ' + key
            key2 = '+ ' + key
            value2 = data2.get(key)
            diff[key1] = value
            diff[key2] = value2
        else:
            key = '- ' + key
            diff[key] = value
    for key, value in data2.items():
        if key not in [key[2:] for key in diff.keys()]:
            key = '+ ' + key
            diff[key] = value
    return dict(sorted(diff.items(), key=lambda tuple:tuple[0][2]))


def get_json(diff):
    result = []
    for key, value in diff.items():
        if isinstance(value, str):
            result.append(f'{key}: {value}')
        else:
            result.append(f'{key}: {json.JSONEncoder().encode(value)}')
    result = '{\n  ' + '\n  '.join(result) + '\n}'
    return result


def generate_diff(file_path1=None, file_path2=None):
    if file_path1 == None and file_path2 == None:
        args = get_args()
        file_path1 = args.first_file
        file_path2 = args.second_file
    diff = find_diff(file_path1, file_path2)
    json = get_json(diff)
    return json
