import heapq

class TimeoutDetector:
    """
        简单版本, 使用pq保存开始时间。
        每次来了一个timestamp, 检查队列是否需要弹出。依赖新日志触发

    """
    def __init__(self, timeout):
        self.timeout = timeout
        self.running = {}  # rpc_id -> start_time
        self.heap = []     # min-heap of (start_time, rpc_id)
        self.timed_out = []

    def start_background_checker(self, interval=1.0):
        def loop():
            current_time = time.time()
            while self.heap and current_time - self.heap[0][0] > self.timeout:
                start_time, rpc_id = heapq.heappop(self.heap)
                self.timed_out.append((rpc_id, start_time, current_time))
                print(f"[Timeout] RPC {rpc_id} timed out (started at {start_time:.2f}, now {current_time:.2f})")

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()

    def process(self, rpc_id, timestamp, event):
        timed_out_ids = []

        if event == "START":
            self.running[rpc_id] = timestamp
            heapq.heappush(self.heap, (timestamp, rpc_id))

        elif event == "END":
            self.running.pop(rpc_id, None)  # remove if exists

        # Check timeout (we do it lazily here)
        while self.heap and timestamp - self.heap[0][0] > self.timeout:
            start_time, rid = heapq.heappop(self.heap)
            if rid in self.running:
                timed_out_ids.append(rid)
                self.running.pop(rid)  # Once timed out, remove it

        return timed_out_ids




import heapq
import time
import threading

class RealTimeTimeoutDetector:
    """
        设置一个后台的timeout检测器。

        def start_background_checker(self, interval=1.0):
            def loop():
                current_time = time.time()
                while self.heap and current_time - self.heap[0][0] > self.timeout:
                    start_time, rpc_id = heapq.heappop(self.heap)
                    self.timed_out.append((rpc_id, start_time, current_time))
                    print(f"[Timeout] RPC {rpc_id} timed out (started at {start_time:.2f}, now {current_time:.2f})")

            thread = threading.Thread(target=loop, daemon=True)
            thread.start()

        current_time = time.time()
        while self.heap and current_time - self.heap[0][0] > self.timeout:
            start_time, rpc_id = heapq.heappop(self.heap)
            self.timed_out.append((rpc_id, start_time, current_time))
            print(f"[Timeout] RPC {rpc_id} timed out (started at {start_time:.2f}, now {current_time:.2f})")

            if rpc_id in self.running:
                self.running.pop(rpc_id)
                self.timed_out.append((rpc_id, start_time, current_time))
                print(f"[Timeout] RPC {rpc_id} timed out (started at {start_time:.2f}, now {current_time:.2f})")

    """
    def __init__(self, timeout):
        self.timeout = timeout
        self.running = {}         # rpc_id -> start_time
        self.heap = []            # min-heap of (start_time, rpc_id)
        self.lock = threading.Lock()
        self.timed_out = []       # list of (rpc_id, start_time, timeout_time)
        self.running_flag = False

    def insert_log(self, rpc_id, event):
        now = time.time()
        with self.lock:
            self._check_timeouts(now)
            if event == "START":
                self.running[rpc_id] = now
                heapq.heappush(self.heap, (now, rpc_id))
            elif event == "END":
                self.running.pop(rpc_id, None)

    def _check_timeouts(self, current_time=None):
        if current_time is None:
            current_time = time.time()
        while self.heap and current_time - self.heap[0][0] > self.timeout:
            start_time, rpc_id = heapq.heappop(self.heap)
            if rpc_id in self.running:
                self.running.pop(rpc_id)
                self.timed_out.append((rpc_id, start_time, current_time))
                print(f"[Timeout] RPC {rpc_id} timed out (started at {start_time:.2f}, now {current_time:.2f})")

    def start_background_checker(self, interval=1.0):
        def loop():
            self.running_flag = True
            while self.running_flag:
                with self.lock:
                    self._check_timeouts()
                time.sleep(interval)

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()

    def stop(self):
        self.running_flag = False

    def get_timeouts(self):
        with self.lock:
            return list(self.timed_out)



timeout = 3
logs = [
    [1, 0, "START"],
    [2, 1, "START"],
    [1, 2, "END"],
    [3, 5, "START"],
    [2, 6, "END"],
    [3, 7, "END"],
]

print_timeout(logs, timeout)