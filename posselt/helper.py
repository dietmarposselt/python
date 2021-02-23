def get_value(data, keys, fallback=None):
    if isinstance(keys, str):
        return get_value(data, keys.split('.'), fallback=fallback)
    d = data
    for key in keys:
        if d is None or key not in d:
            return fallback
        d = d[key]
    return d

def get_or_create(data, key, initial):
    if key not in data:
        data[key] = initial
    return data[key]
