"""
input: [1,2,3,4,5] output: '[1, 2, 3, 4, 5]'
input: {"data": 300} output: '{"data": 300}'
input: 35 output: '35'
一共要转换的有6种类型：dict, list, str, bool, num, None。
大致思路就是primitive类型直接在两边加""，对于dict和list就要先加“[”, “{”，再遍历，同时加进去","。
要注意的是dict和list里面的数据可以是其他类型，用递归就行了。
"""


def serialize(value):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        return "[" + ", ".join(serialize(item) for item in value) + "]"
    elif isinstance(value, dict):
        items = []
        for k, v in value.items():
            key_str = serialize(k)
            val_str = serialize(v)
            items.append(f"{key_str}: {val_str}")
        return "{" + ", ".join(items) + "}"
    else:
        raise TypeError(f"Unsupported type: {type(value)}")


print({"data": {"abc": [1,2,34], "def": 400}})