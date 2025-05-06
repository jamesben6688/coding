def once(fn):
    called = False
    result = None

    def wrapper(*args, **kwargs):
        nonlocal called, result
        if not called:
            result = fn(*args, **kwargs)
            called = True
        return result

    return wrapper


def add(a, b):
    print("Function is called!")
    return a + b

once_add = once(add)

print(once_add(2, 3))  # 输出: Function is called! → 5
print(once_add(100, 200))  # 没有输出“Function is called!”，返回还是 5
print(once_add(999, 999))  # 返回依旧是 5
