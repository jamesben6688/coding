"""
要求写一个csv parser，后续问题是csv中的某个单元格可能包含“，”如何处理。

标准CSV格式规定：

如果一个单元格中含有逗号，需要用双引号 " 把整个单元格括起来。

例如：
John,"Smith, Jr.",25
应该被解析为
["John", "Smith, Jr.", "25"]

所以 不能简单直接 split(',')，而是需要识别：

在 引号内的逗号 不算分隔符

只有在 引号外的逗号 才是分隔符
"""


def parse_csv(csv_text: str):
    rows = csv_text.strip().split('\n')
    result = []

    for row in rows:
        fields = []
        field = ''
        in_quotes = False

        for i, char in enumerate(row):
            if char == '"':
                in_quotes = not in_quotes  # 遇到引号切换状态
            elif char == ',' and not in_quotes:
                fields.append(field)
                field = ''
            else:
                field += char

        fields.append(field)  # 加入最后一个field
        result.append(fields)

    return result


csv_text = '''John,Smith,25
Alice,"Wonder, Land",30
"Bob, Jr.","New York, NY",40'''

for row in parse_csv(csv_text):
    print(row)
