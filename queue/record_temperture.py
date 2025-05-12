from collections import deque

class TemperatureTracker:
    def __init__(self):
        self.capacity = 86400  # 24 hours in seconds
        self.temps = deque()
        self.total = 0
        self.max_queue = deque()  # monotonic queue for max tracking

    def add_temperature(self, temp: float):
        # Add new temp
        self.temps.append(temp)
        self.total += temp

        # Maintain monotonic decreasing queue for max
        while self.max_queue and self.max_queue[-1] < temp:
            self.max_queue.pop()
        self.max_queue.append(temp)

        # Remove oldest if over 24hr
        if len(self.temps) > self.capacity:
            old = self.temps.popleft()
            self.total -= old
            if old == self.max_queue[0]:
                self.max_queue.popleft()

    def get_average(self) -> float:
        if not self.temps:
            return 0.0
        return self.total / len(self.temps)

    def get_max(self) -> float:
        if not self.max_queue:
            return float('-inf')
        return self.max_queue[0]
