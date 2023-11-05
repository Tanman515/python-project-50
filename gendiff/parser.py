def sort(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[0][1:]))


def add_spaces(d):
    result = {}
    for key, value in d.items():
        if key[0] not in ('+', '-', ' '):
            key = f'  {key}'
        if isinstance(value, dict):
            result[key] = add_spaces(value)
        else:
            result[key] = value
    return result


def parse(data1, data2): # noqa C901
    result = {}
    for key, value in data2.items():
        if key not in data1:
            result[f'+ {key}'] = value

    for key, value in data1.items():
        if key not in data2.keys():
            result[f'- {key}'] = value
            continue

        if not isinstance(value, dict):
            if value == data2.get(key):
                result[f'  {key}'] = value
            else:
                result[f'- {key}'] = value
                result[f'+ {key}'] = data2.get(key)
        else:
            if isinstance(data2.get(key), dict):
                result[f'  {key}'] = parse(value, data2.get(key))
            else:
                result[f'- {key}'] = value
                result[f'+ {key}'] = data2.get(key)
    return add_spaces(sort(result))
