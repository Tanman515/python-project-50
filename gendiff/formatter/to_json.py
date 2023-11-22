import json


def make_json(view):
    return json.dumps(view, indent=2, sort_keys=True)
