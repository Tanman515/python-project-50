import json


def key_for_sort(text):
    path = text.split(' ')[1][1:-1]
    if '.' in path:
        sort_value = ''.join(path.split('.'))
    else:
        sort_value = path
    return sort_value


def plain(diff): # noqa
    result = []

    def walk(node, path):
        for key, value in node.items():
            path.append(key)
            if isinstance(value, tuple):
                category = value[0]
                full_path = '.'.join(path)
                if category == 'added':
                    if isinstance(value[1], dict):
                        value = '[complex value]'
                    elif isinstance(value[1], str):
                        value = f"'{value[1]}'"
                    else:
                        value = json.JSONEncoder().encode(value[1])
                    result.append(f"Property '{full_path}' was added with value: {value}") # noqa
                elif category == 'removed':
                    result.append(f"Property '{full_path}' was removed") # noqa
                elif category == 'changed':
                    if isinstance(value[1], dict):
                        value1 = '[complex value]'
                    elif isinstance(value[1], str):
                        value1 = f"'{value[1]}'"
                    else:
                        value1 = json.JSONEncoder().encode(value[1])

                    if isinstance(value[2], dict):
                        value2 = '[complex value]'
                    elif isinstance(value[2], str):
                        value2 = f"'{value[2]}'"
                    else:
                        value2 = json.JSONEncoder().encode(value[2])
                    result.append(f"Property '{full_path}' was updated. From {value1} to {value2}") # noqa
                else:
                    if isinstance(value[1], dict):
                        walk(value[1], path)
            if isinstance(value, dict):
                walk(value, path)
            path.pop()
    walk(diff, [])
    return '\n'.join(sorted(result, key=key_for_sort))
