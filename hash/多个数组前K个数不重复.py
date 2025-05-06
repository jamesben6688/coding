"""
给两个list, listA, listB, 和一个整数k, 删除listB中的元素使新的listB 的前k个数与listA前k个数无相同的数
遍历方法做出来了，刚开始想不到特定题型就说用brute force遍历，面试官说可以继续写
Followup1: 时间复杂度O(n)

Followup2: 如果不止两个list， 而是list of lists, 一个整数k，还有一个整数d，d表示对于每个list，它与前d个lists的前k个数都不能有重复。
这个花了点时间理解题目，问了很多clarification question，
刚开始还是没有具体思路写了个draft。面试官提示了之后改了一部分。最后时间到了没有做完但是写了思路comment

"""

class Solution:
    def twolist(self, list1, list2, k):
        set1 = set(list1[:k])

        to_remove = []
        cnt = 0
        for i in range(len(list2)):
            if cnt == k:
                break
            if list2[i] in set1:
                pass
            else:
                list2[cnt] = list2[i]
                cnt += 1

        return list2, cnt

    def multi_list(self, lists, k, d):
        s = set()
        n = len(lists)
        ans = []
        for i in range(n):
            l = lists[i]
            cnt = 0
            if i-d-1 >= 0:
                del_list = lists[i-d-1]

                for j in range(ans[i-d-1]):
                    s.remove(del_list[j])

            for kk in range(len(l)):
                if cnt == k:
                    break
                if l[kk] not in s:
                    l[cnt] = l[kk]
                    cnt += 1
                    s.add(l[kk])

            ans.append(cnt)

        return lists, ans


print(Solution().twolist(
    [1, 2, 3],
    [2, 3, 4],
    k = 2
))

print(Solution().multi_list(
lists = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
],
k = 2,
d = 1
# list[1] 前2个有2与 list[0] 冲突，要删除 2 或 3
# list[2] 前2个有4与 list[1] 冲突，要删


))