import json


def make_comfort(d):
    result = {}
    i = 0
    keys = list(d.keys())
    while i < len(d):
        if keys[i][0] == '-' and i < len(d) - 1:
            if keys[i][1:] == keys[i+1][1:]:
                value = (d[keys[i]], d[keys[i+1]])
                result[f'-+{keys[i][2:]}'] = value
                i += 2
            else:
                result[keys[i]] = d[keys[i]]
                i += 1
                continue
        elif keys[i][0] == ' ' and isinstance(d[keys[i]], dict):
            result[keys[i]] = make_comfort(d[keys[i]])
            i += 1
        else:
            result[keys[i]] = d[keys[i]]
            i += 1
    return result


def plain(view): # noqa C901
    result = []

    def walk(node, path):
        for key, value in node.items():
            path.append(key[2:])
            if key[:2] == '- ':
                full_path = '.'.join(path)
                result.append(f"Property '{full_path}' was removed") # noqa
            elif key[:2] == '+ ':
                full_path = '.'.join(path)
                if isinstance(value, dict):
                    value = '[complex value]'
                elif isinstance(value, str):
                    value = f"'{value}'"
                else:
                    value = json.JSONEncoder().encode(value)
                result.append(f"Property '{full_path}' was added with value: {value}") # noqa
            elif key[:2] == '-+':
                full_path = '.'.join(path)
                if isinstance(value[0], dict):
                    value1 = '[complex value]'
                elif isinstance(value[0], str):
                    value1 = f"'{value[0]}'"
                else:
                    value1 = json.JSONEncoder().encode(value[0])

                if isinstance(value[1], dict):
                    value2 = '[complex value]'
                elif isinstance(value[1], str):
                    value2 = f"'{value[1]}'"
                else:
                    value2 = json.JSONEncoder().encode(value[1])
                result.append(f"Property '{full_path}' was updated. From {value1} to {value2}") # noqa
            else:
                if isinstance(value, dict):
                    walk(value, path)
            path.pop()
    walk(make_comfort(view), [])
    return '\n'.join(result)
