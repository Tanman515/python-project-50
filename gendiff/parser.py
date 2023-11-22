import json
import yaml


def parse(data1, data2, type): # noqa
    if type == 'json':
        data1 = json.loads(data1)
        data2 = json.loads(data2)
    elif type == 'yaml':
        data1 = yaml.load(data1, Loader=yaml.FullLoader)
        data2 = yaml.load(data2, Loader=yaml.FullLoader)
    else:
        pass
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
                result[key] = ('same', parse(value, data2.get(key), 'None'))
            else:
                result[key] = ('changed', value, data2.get(key))
    return result
