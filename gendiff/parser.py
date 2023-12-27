import json
import yaml


def parse(data, type):
    if type == 'json':
        data = json.loads(data)
    elif type == 'yaml':
        data = yaml.load(data, Loader=yaml.FullLoader)
    return data
