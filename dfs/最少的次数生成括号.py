"""
给你一组括号，比如 "( ("，然后你可以add delete或者replace三种操作，然后用最少的操作得到一个平衡的括号string，输入是一个string，
输出是一个list of string。前面这个例子显然是replace一次最优，输出 "( )"。
再举个例子："( ( ) ( )"，这个输出是 "( ) ( ) ( )", "( ( ) ( ) )", "( ) ( )"。

这题用Bfs
"""
def find_invalid_positions(s):
    stack = []          # 存左括号 '(' 的 index
    invalid = set()     # 存右括号 ')' 的 index（没匹配成功）

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()  # 匹配一个左括号
            else:
                invalid.add(i)  # 多余的右括号

    # stack 中剩下的 index 是多余的左括号
    invalid.update(stack)
    return invalid

def generate_valid_strings(s, invalid_set):
    from itertools import combinations
    results = set()
    invalid_list = sorted(invalid_set)
    min_ops = [float('inf')]  # 全局记录最少修改数
    results = set()

    def dfs(pos, path, invalid_used, balance):
        """
        pos	    int	当前处理到的字符串下标（索引位置）
        path	str	当前构造出来的中间字符串路径（合法性构造的进展）
        invalid_used	int	当前已经使用的“修改操作”次数（可用于剪枝）
        balance	int	括号当前的“平衡度”：有多少未闭合的 '('
        :param pos:
        :param path:
        :param invalid_used:
        :param balance:
        :return:
        """
        if balance < 0: return
        if pos == len(s):
            if balance == 0:
                if invalid_used < min_ops[0]:
                    results.clear()
                    min_ops[0] = invalid_used
                    results.add(path)
                elif invalid_used == min_ops[0]:
                    results.add(path)
            return

        if pos in invalid_set:
            # DELETE
            dfs(pos + 1, path, invalid_used + 1, balance)

            if s[pos] == '(':
                # REPLACE (only if it makes sense)
                dfs(pos + 1, path + ')', invalid_used + 1, balance - 1)

                # don't do anything
                dfs(pos + 1, path + '(', invalid_used, balance + 1)

            elif s[pos] == ')':
                # replace
                dfs(pos + 1, path + '(', invalid_used + 1, balance + 1)

                # don't do anything
                dfs(pos + 1, path + ')', invalid_used, balance - 1)

        else:
            if s[pos] == '(':
                dfs(pos + 1, path + '(', invalid_used, balance + 1)
            elif s[pos] == ')':
                if balance > 0:
                    dfs(pos + 1, path + ')', invalid_used, balance - 1)
            else:
                dfs(pos + 1, path + s[pos], invalid_used, balance)

    dfs(0, "", 0, 0)
    return list(results)


def fix_invalid_parentheses(s):
    invalid_positions = find_invalid_positions(s)
    return generate_valid_strings(s, invalid_positions)


# print(fix_invalid_parentheses("(("))               # ['()']
# print(fix_invalid_parentheses("(()())"))           # ['(()())']
# print(fix_invalid_parentheses("(()(()"))           # ['(())()', '(()())']
print(fix_invalid_parentheses("(()()"))        # ['( ) ( ) ( )', '( ) ( )', '( ( ) ( ) )']
