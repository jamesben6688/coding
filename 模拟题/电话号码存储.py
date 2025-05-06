"""
假设你有一个phonenumber的存储
实现
1.number insert to db
2.is number taken
3.give a new number
这个phonenumber会很大的情况下会怎么设计用什么来存储以及实现
"""

import heapq
from bitarray import bitarray  # 或用 roaringbitmap 库

class PhoneNumberManager:
    def __init__(self, max_number=10**10):
        self.max_number = max_number
        self.bitmap = bitarray(max_number)
        self.bitmap.setall(0)
        self.recycled = []
        self.next = 0

    def insert(self, number: int) -> bool:
        if self.bitmap[number]:
            return False
        self.bitmap[number] = True
        return True

    def is_taken(self, number: int) -> bool:
        return self.bitmap[number]

    def get_new_number(self) -> int:
        while self.recycled:
            num = heapq.heappop(self.recycled)
            if not self.bitmap[num]:
                self.bitmap[num] = True
                return num

        while self.next < self.max_number:
            if not self.bitmap[self.next]:
                self.bitmap[self.next] = True
                res = self.next
                self.next += 1
                return res
            self.next += 1

        raise RuntimeError("No available numbers")

    def release(self, number: int):
        if self.bitmap[number]:
            self.bitmap[number] = False
            heapq.heappush(self.recycled, number)
