class SyntaxException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

def parse(s, index, sign):
    num1, num2 = 0, 0
    i = index
    # para 1
    if s[i:].startswith("+("):
        num1, i = parse(s, i+2, "+")
    elif s[i:].startswith("-("):
        num1, i = parse(s, i+2, "-")
    elif s[i:].startswith("*("):
        num1, i = parse(s, i+2, "*")
    elif s[i:].startswith("/("):
        num1, i = parse(s, i+2, "/")
    elif s[i].isdigit():
        while i < len(s) and s[i].isdigit():
            num1 = num1 * 10 + int(s[i])
            i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i+3]}")
    # comma
    if i == len(s):
        return num1, i
    elif s[i] == ",":
        i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i+3]}")
    # para 2
    if s[i:].startswith("+("):
        num2, i = parse(s, i+2, "+")
    elif s[i:].startswith("-("):
        num2, i = parse(s, i+2, "-")
    elif s[i:].startswith("*("):
        num2, i = parse(s, i+2, "*")
    elif s[i:].startswith("/("):
        num2, i = parse(s, i+2, "/")
    elif s[i].isdigit():
        while i < len(s) and s[i].isdigit():
            num2 = num2 * 10 + int(s[i])
            i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i+3]}")
    if s[i] == ')':
        if sign == "+":
            return num1+num2, i+1
        elif sign == "-":
            return num1-num2, i+1
        elif sign == "*":
            return num1*num2, i+1
        elif sign == "/":
            if int(num2) == 0:
                raise DivisionByZeroException(f"division by zero at {i}: {s[i:i+3]}")
            return num1/num2, i+1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i+3]}")


def cal(s):
    s = s.replace(" ", "")
    num, i = parse(s, 0, "+")
    return num

print(cal("+(3, 3, 3)"))
