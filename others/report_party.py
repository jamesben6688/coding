from collections import defaultdict
from collections import deque


"""
要实时检测数据流中的 party 事件，我们可以通过滑动窗口（sliding window）技术来处理每个用户在各个地点的活动记录，并及时检测是否满足 "party" 的条件：某个 place_id 在过去 60 分钟内一直有至少 100 个人。以下是如何设计这个系统的思路。

系统需求回顾：
实时处理：数据流是实时到达的，我们需要实时处理这些事件，而不能依赖于批量报告。

用户活动记录：每个用户的活动是 (user_id, timestamp, place_id)，记录了用户在某个时间出现在某个地点。

party 事件：如果在某个 place_id 上有至少 100 个不同的用户在过去 60 分钟内访问过这个地方，则视为发生了一个 "party" 事件。

解决方案设计：
1. 滑动窗口：
由于 party 事件的判断需要查看过去 60 分钟的数据，所以我们需要使用滑动窗口来保存最近 60 分钟内的数据。这要求我们能够实时更新窗口中的活动记录。

2. 数据结构选择：
使用一个字典或哈希表来记录每个 place_id 和每个时间段内的用户集合。

每个 place_id 对应一个哈希表，哈希表的键是 user_id，值是该用户的最后访问时间（timestamp）。

通过维护每个 place_id 上的用户数据，我们能够快速判断是否满足 "party" 事件的条件。

3. 实时检测：
每当一个新的事件 (user_id, timestamp, place_id) 到来时，首先更新该 place_id 上用户的访问时间。

然后移除 60 分钟之前的用户记录，这样我们总是能够保持每个 place_id 最近 60 分钟的访问记录。

最后检查该 place_id 上在 60 分钟内的独立用户数，如果至少有 100 个不同的用户，则触发 "party" 事件。
"""


class PartyEventDetector:
    def __init__(self):
        # 存储每个 place_id 中的用户及其访问时间
        self.place_user_map = defaultdict(dict)
        # 用于检查最近 60 分钟的时间窗口
        self.time_window = 60  # 60 minutes

    def report(self, user_id, timestamp, place_id):
        # 更新该用户的访问记录
        self.place_user_map[place_id][user_id] = timestamp

        # 清除超出 60 分钟的历史记录
        self.clean_old_records(place_id, timestamp)

        # 检查是否满足 party 事件条件
        if self.check_party_event(place_id, timestamp):
            print(f"Party detected at place_id {place_id} at time {timestamp}")

    def clean_old_records(self, place_id, timestamp):
        # 清除过期的用户记录，超过 60 分钟的记录
        to_remove = []
        for user_id, visit_time in self.place_user_map[place_id].items():
            if timestamp - visit_time > self.time_window:
                to_remove.append(user_id)

        for user_id in to_remove:
            del self.place_user_map[place_id][user_id]

    def check_party_event(self, place_id, timestamp):
        # 检查当前 place_id 在过去 60 分钟内是否有至少 100 个不同的用户
        unique_users = len(self.place_user_map[place_id])
        return unique_users >= 100


# 示例使用：
detector = PartyEventDetector()

# 假设我们有以下的数据流
events = [
    (1, 100, "A"),
    (2, 101, "A"),
    (3, 102, "A"),
    # ... 更多数据流事件
]

# 逐一报告数据流事件
for event in events:
    user_id, timestamp, place_id = event
    detector.report(user_id, timestamp, place_id)
