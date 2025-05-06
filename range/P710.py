import bisect

class RangeModule:

    def __init__(self):
        """
            题解: https://www.bilibili.com/video/BV1zQ4y187uF/?spm_id_from=333.1391.0.0&vd_source=515dedd17a7416a93307429c1b2dfa6b
            [
                a1, a2, a3, a4....
            ]
        """
        self.range = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.range, left)
        end = bisect.bisect_right(self.range, right)

        tmp = []
        if start % 2 == 0:
            tmp.append(left)
        if end % 2 == 0:
            tmp.append(right)

        """
            tmp为空表示直接把左右连接起来
            
            start为奇数, 说明新区间的左边界已经在range里, 不用管他
            start为偶数, 新区间的左边界在两个区间之间, 需要加入
            
            end为奇数, 说明新区间有边界已经在range里, 不用管
            end为偶数, 新区间的右边界在两个区间之间, 需要加入
            
            [start:end]为需要改变的区间
        """
        self.range[start:end] = tmp

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.range, left)
        end = bisect.bisect_left(self.range, right)

        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.range, left)
        end = bisect.bisect_right(self.range, right)

        tmp = []
        if start % 2 == 1:
            tmp.append(left)
        if end % 2 == 1:
            tmp.append(right)

        self.range[start:end] = tmp

# ops = ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
# params = [[],[10,20],[14,16],[10,14],[13,15],[16,17]]

# ops = ["RangeModule","addRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","queryRange"]
# params = [[],[10,180],[150,200],[250,500],[50,100],[180,300],[600,1000],[50,150],[50,100]]

# ops = ["RangeModule","addRange","queryRange","removeRange","removeRange","addRange","queryRange","addRange","queryRange","removeRange"]
# params = [[],[5,8],[3,4],[5,6],[3,6],[1,3],[2,3],[4,8],[2,3],[4,9]]

ops = ["RangeModule","addRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange"]
params = [[],[6,8],[7,8],[8,9],[8,9],[1,3],[1,8],[2,4],[2,9],[4,6]]
# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
for i in range(1, len(ops)):

    if 'add' in ops[i]:
        obj.addRange(*params[i])
    elif 'remove' in ops[i]:
        obj.removeRange(*params[i])
    else:
        print(obj.queryRange(*params[i]))
    print(ops[i], params[i], obj.range)


# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)