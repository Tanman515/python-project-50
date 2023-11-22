import json


def sort(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[0][1:]))


def make_string(value, replacer=' ', indent=2):
    def walk(node, counter):
        replacer_value = replacer * indent * counter
        replacer_value_before_end = replacer * indent * (counter - 1)
        begin = ['{']
        end = replacer_value_before_end + '}'
        middle_values = []
        for key, value in node.items():
            if isinstance(value, dict):
                value = walk(value, counter + 2)
            elif not isinstance(value, str):
                value = json.JSONEncoder().encode(value)
            middle_values.append(f'{replacer_value}{key}: {value}')
        result = begin + middle_values + [end]
        return '\n'.join(result)
    return walk(value, 1)


def add_spaces(d):
    result = {}
    for key, value in d.items():
        key = f'  {key}'
        if isinstance(value, dict):
            result[key] = add_spaces(value)
        else:
            result[key] = value
    return result


def make_dict(view): # noqa
    result = {}
    for key, value in view.items():
        if isinstance(value, tuple):
            category = value[0]
            if category == 'added':
                if isinstance(value[1], dict):
                    value = make_dict(value[1])
                else:
                    value = value[1]
                result[f'+ {key}'] = value
            elif category == 'removed':
                if isinstance(value[1], dict):
                    value = make_dict(value[1])
                else:
                    value = value[1]
                result[f'- {key}'] = value
            elif category == 'same':
                if isinstance(value[1], dict):
                    value = make_dict(value[1])
                else:
                    value = value[1]
                result[f'  {key}'] = value
            elif category == 'changed':
                first_value = value[1]
                second_value = value[2]
                if isinstance(first_value, dict):
                    result[f'- {key}'] = make_dict(first_value)
                else:
                    result[f'- {key}'] = first_value
                if isinstance(second_value, dict):
                    result[f'+ {key}'] = make_dict(second_value)
                else:
                    result[f'+ {key}'] = second_value
        elif isinstance(value, dict):
            result[f'  {key}'] = add_spaces(value)
        else:
            result[f'  {key}'] = value
    return sort(result)


def make_stylish(diff):
    dictionary = make_dict(diff)
    stylish_format = make_string(dictionary)
    return stylish_format
