from collections import Counter


def most_talkative_person(chat_history):
    # 初始化一个字典来记录每个人的发言次数
    # talk_count = {}
    talk_count = Counter()

    # 遍历每条聊天记录
    for record in chat_history:
        talk_count[record['name']] += len(record['message'].split(" "))
        # name = record['name']
        # message = record['message']
        #
        # # 更新该人的发言次数
        # if name in talk_count:
        #     talk_count[name] += 1
        # else:
        #     talk_count[name] = 1

    # 找到发言次数最多的人
    # most_talkative = max(talk_count, key=talk_count.get)
    mx_name = ""
    mx_cnt = 0
    for name in talk_count:
        if talk_count[name] > mx_cnt:
            mx_cnt = talk_count[name]
            mx_name = name
    return mx_name, mx_cnt


# 示例输入
chat_history = [
    {"name": "Alice", "message": "Hi, how are you?"},
    {"name": "Bob", "message": "I'm good, thanks! How about you?"},
    {"name": "Alice", "message": "I'm doing well too."},
    {"name": "Alice", "message": "What have you been up to?"},
    {"name": "Bob", "message": "Just working on some stuff."},
    {"name": "Charlie", "message": "Hey everyone!"},
    {"name": "Alice", "message": "Good to hear!"}
]

# 调用函数
most_talkative, count = most_talkative_person(chat_history)
print(f"The most talkative person is {most_talkative} with {count} messages.")