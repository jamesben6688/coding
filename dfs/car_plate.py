class Solution:
    """
        以 1 为 a1(首字母) 的排列一共有 (n−1)! 个；
        以 2 为 a1(首字母)的排列一共有 (n−1)! 个；

        以 n 为 a1的排列一共有 (n−1)! 个。

        由于我们需要求出从小到大的第 k 个排列，因此：

        如果 k≤(n−1)! ，我们就可以确定排列的首个元素为 1；
        如果 (n−1)!< k ≤2⋅(n−1)! 我们就可以确定排列的首个元素为 2；
    """

    def get_fac(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def getPermutation(self, n: int, k: int) -> str:
        res = []

        num = list(range(1, n + 1))

        k -= 1
        res = ""
        for i in range(n):
            fac = self.get_fac(len(num) - 1)
            d = k // fac
            res += str(num[d])
            num.pop(d)
            k = k % fac

        return res

