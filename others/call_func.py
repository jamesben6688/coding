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
    print("Function called!")
    return a + b

once_add = once(add)

print(once_add(2, 3))  # Output: "Function called!" + 5
print(once_add(10, 20))  # Output: 5 (no new call, same result)

