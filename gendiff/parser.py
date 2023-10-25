def parse(data1, data2):
    diff = {}
    for key, value in data1.items():
        if value == data2.get(key) and key in data2.keys():
            key = '  ' + key
            diff[key] = value
        elif value != data2.get(key) and key in data2.keys():
            key1 = '- ' + key
            key2 = '+ ' + key
            value2 = data2.get(key)
            diff[key1] = value
            diff[key2] = value2
        else:
            key = '- ' + key
            diff[key] = value
    for key, value in data2.items():
        if key not in [key[2:] for key in diff.keys()]:
            key = '+ ' + key
            diff[key] = value
    return dict(sorted(diff.items(), key=lambda tuple: tuple[0][2]))
