"""
    判断是否合法

"""
def evaluate_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            try:
                stack.append(int(token))
            except ValueError:
                return "Invalid: Non-numeric operand"
        else:
            if len(stack) < 2:
                return "Invalid: Not enough operands"
            b = stack.pop()
            a = stack.pop()
            try:
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        return "Invalid: Division by zero"
                    # Python 的 / 会产生浮点数，我们做整数除法
                    stack.append(int(a / b))
            except Exception as e:
                return f"Invalid: {e}"

    if len(stack) != 1:
        return "Invalid: Extra operands remaining"
    return stack[0]
