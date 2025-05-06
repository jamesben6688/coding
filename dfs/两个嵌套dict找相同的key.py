"""
coding 两个dictionary，每个dictionary 都是key 然后套一个或多个dictionary
要求找到两个dictionary相同的key 和独立的key（要把所有的dictionary展开到最里
层去比较）
"""
def flatten_keys(d, prefix=''):
    keys = set()
    for k, v in d.items():
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            keys |= flatten_keys(v, path)
        else:
            keys.add(path)
    return keys

def compare_dict_keys(dict1, dict2):
    keys1 = flatten_keys(dict1)
    keys2 = flatten_keys(dict2)

    common = keys1 & keys2
    only_in_1 = keys1 - keys2
    only_in_2 = keys2 - keys1

    return {
        "common": sorted(common),
        "only_in_dict1": sorted(only_in_1),
        "only_in_dict2": sorted(only_in_2)
    }
