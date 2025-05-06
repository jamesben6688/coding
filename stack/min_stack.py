class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        x = self.stack.pop()
        if self.min_stack and x == self.min_stack[-1]:
            self.min_stack.pop()

        return x

    def get_min(self):
        return self.min_stack[-1]


s = Solution()
s.push(2)
s.push(3)
s.push(4)

print(s.get_min())
print(s.pop())
print(s.get_min())
