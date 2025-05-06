"""
Q2. 给一个聊天系统，要求实现两个函数
第一个函数是每个两个用户之间有新消息时都有 call 这个函数：register_event(int timestamp, string sender, string receiver, string msg)
第二个函数是要求获得有最多 open chat 的用户，两个用户之间一旦有过消息，就视为open chat，且永远不会关闭：get_most_active_user()
Followup 是实现删除用户，delete_user(string username)，感觉这个题目就是变种 LFU
"""
from collections import defaultdict


class Chat:
    def __init__(self):
        self.chats = defaultdict(lambda : defaultdict(list))

    def register_event(self, t, sender, receiver, msg):
        self.chats[sender][receiver].append(msg)
        self.chats[receiver][sender].append(msg)

    def get_most_active_user(self):
        ans = ""
        mx = 0
        for user in self.chats:
            chats = 0
            for receiver in self.chats[user]:
                chats += len(self.chats[user][receiver])

            if chats > mx:
                mx = chats
                ans = user

        return user

    def delete_user(self, username):
        receiver = list(self.chats[username].keys())
        for r in receiver:
            self.chats[r].pop(username)

        self.chats.pop(username)



