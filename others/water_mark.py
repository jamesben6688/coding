class Solution:
    def __init__(self, initialHighWaterMark: int):
        self.hwm = initialHighWaterMark  # 当前水位线
        self.processed = set()           # 已处理请求集合

    def processRequest(self, requestId: int):
        self.processed.add(requestId)
        # 尝试提升水位线
        while self.hwm + 1 in self.processed:
            self.hwm += 1

    def getCurrentHighWaterMark(self) -> int:
        return self.hwm