from collections import deque, defaultdict


class MessageHandler:
    def __init__(self, window_size=10):
        # 初始化队列和集合
        self.window_size = window_size  # 时间窗口大小，单位为秒
        self.messages = defaultdict(deque)  # 队列，存储消息和时间戳

    def print_message(self, message, timestamp):
        if message in self.messages and timestamp - self.messages[message][-1] < self.window_size:
            pass
            self.messages[message].pop()
            if len(self.messages[message]) == 0:
                self.messages.pop(message)
        else:
            # print(message, timestamp)
            self.messages[message].append(timestamp)


# 示例
handler = MessageHandler()

# 模拟消息和时间戳
messages = [
    ("Hello", 1),
    ("Hi", 5),
    ("Hello", 8),
    ("Hello", 12),
    ("Hi", 15),
    ("Hello", 16),
    ("Hi", 18)
]

for msg, ts in messages:
    handler.print_message(msg, ts)

print(handler.messages)