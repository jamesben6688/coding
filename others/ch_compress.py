"""
https://www.1point3acres.com/bbs/thread-1110663-1-1.html
1. 压缩字符串
2. 用栈实现队列
"""
class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.num = 0
        self.ch = ''
        self.s = compressedString

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.s[self.idx]
            self.idx += 1

            while self.idx < len(self.s) and self.s[self.idx].isdigit():
                self.num = 10 * self.num + int(self.s[self.idx])
                self.idx += 1
        self.num -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.idx != len(self.s) or self.num != 0


s = StringIterator('L1e2t1C1o1d1e1')
print(s.next())