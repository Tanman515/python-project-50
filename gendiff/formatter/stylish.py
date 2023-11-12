import json


def stylish(value, replacer=' ', indent=2):
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
