import json


def make_json(diff):
    result = []
    for key, value in diff.items():
        if isinstance(value, str):
            result.append(f'{key}: {value}')
        else:
            result.append(f'{key}: {json.JSONEncoder().encode(value)}')
    result = '{\n  ' + '\n  '.join(result) + '\n}'
    return result
