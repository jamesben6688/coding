from collections import defaultdict


class PartyDetector:
    def __init__(self, windows=60):
        """
            {
                place_id: {user_id: timestamp}
            }

        """
        self.places = defaultdict(defaultdict)
        self.user_places = defaultdict(str)  # {user_id: place_id}
        self.window = windows

    def report(self, user_id, timestamp, place_id):
        if user_id in self.user_places:
            old_place = self.user_places[user_id]
            self.places[old_place].pop(user_id)
        self.places[place_id].update({user_id: timestamp})

    def detect_party(self, timestamp):
        for place_id, user_times in self.places.items():
            for user_id, t in user_times.items():
                if t < timestamp - self.window:
                    # to_remove.append(user_id)
                    self.places.pop(user_id)

            users = list(set(self.places[place_id].keys()))

            if len(users) >= 3:
                print(f"found party at place: {place_id} from time {timestamp-self.window} to {timestamp}")

def got_data(data_source=""):
    return None, None, None

party_detector = PartyDetector()


import time

# 每分钟检查是否有 party 事件
cur_time = 1000
while True:
# for current_time in range(1000, 1062):
    # 模拟报告数据流
    user_id, timestamp, place_id = got_data()
    assert cur_time == timestamp, 'invalid timestamp'
    if user_id:
        party_detector.report(user_id, timestamp, place_id)

    party_detector.detect_party(cur_time)
    time.sleep(1)  # 模拟 1 秒钟的延迟，表示每次都在不同的时间戳运行检测
    cur_time += 1
