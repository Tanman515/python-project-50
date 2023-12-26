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
    return data1, data2
