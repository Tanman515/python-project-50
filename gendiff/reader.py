import json
import yaml
from yaml.loader import SafeLoader


def read(path):
    data = None
    file_type = path.split('.')[-1]
    if file_type == 'yaml' or file_type == 'yml':
        with open(path) as f:
            data = yaml.load(f, Loader=SafeLoader)
    elif file_type == 'json':
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    return data
