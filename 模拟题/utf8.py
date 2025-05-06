"""
393
"""
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        left = 0
        for d in data:  # 11000101
            if left == 0:
                if d >> 3 == 0b11110:
                    left = 3
                elif d >> 4 == 0b1110:
                    left = 2
                elif d >> 5 == 0b110:
                    left = 1
                elif d >> 7 == 0:
                    left = 0
                else:
                    return False
            else:
                left -= 1
                if d >> 6 == 0b10:
                    continue
                else:
                    return False
        return left == 0


print(Solution().validUtf8([197,130,1]))