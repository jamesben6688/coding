def calculate(expr):
    if isinstance(expr, int):
        return expr

    if isinstance(expr, str):
        expr = expr.strip()
        if expr.isdigit() or (expr.startswith('-') and expr[1:].isdigit()):
            return int(expr)

        # 提取操作符和参数
        if not (expr.startswith('+') or expr.startswith('-') or expr.startswith('*') or expr.startswith('/')):
            raise ValueError(f"Unsupported operator in expression: {expr}")
        if '(' not in expr or not expr.endswith(')'):
            raise ValueError(f"Invalid format: {expr}")

        op = expr[0]
        args_str = expr[2:-1]
        args = split_args(args_str)

        if len(args) != 2:
            raise ValueError(f"Operator '{op}' requires exactly 2 arguments, but got {len(args)}")

        left = calculate(args[0])
        right = calculate(args[1])

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        else:
            raise ValueError(f"Unknown operator: {op}")

    raise ValueError(f"Invalid expression: {expr}")

def split_args(s):
    args = []
    depth = 0
    current = ""
    for c in s:
        if c == ',' and depth == 0:
            args.append(current.strip())
            current = ""
        else:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            current += c
    if current:
        args.append(current.strip())
    return args

# 示例调用：
print(calculate("+(2,5)"))           # 输出 7
print(calculate("-(3,*(4,1))"))      # 输出 -1
print(calculate("0"))               # 输出 0
# print(calculate("+(3,3,3)"))         # 应抛出异常
