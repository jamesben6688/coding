class Solution:
    def min_pos(self, s):
        """
            枚举

        :param s:
        :return:
        """
        mn_cnt = float('inf')
        ans = float('inf')
        # start_idx = float('inf')
        def valid(s):
            i = 0
            idx = -1
            while i < len(s):
                if s[i] == '1':
                    idx = i
                elif s[i] == '0' and idx != -1:
                    if i > idx:
                        return False

                i += 1

            return True

        def dfs(idx, cnt, start_idx):
            nonlocal ans, mn_cnt
            if not valid(s[:idx]):
                return

            if idx == len(s):
                if cnt < mn_cnt:
                    mn_cnt = cnt
                    ans = start_idx
                elif cnt == mn_cnt:
                    if start_idx < ans:
                        ans = start_idx
                return

            if s[idx] == '0':
                s[idx] = '1'
                dfs(idx+1, cnt+1, min(idx, start_idx))
                s[idx] = '0'

                dfs(idx+1, cnt, start_idx)
            if s[idx] == '1':
                s[idx] = '0'
                dfs(idx+1, cnt+1, start_idx)

                s[idx] = '1'
                dfs(idx+1, cnt, min(start_idx, idx))

        dfs(0, 0, float('inf'))

        # print(ans)
        return ans, mn_cnt


print(Solution().min_pos(list('0100001001')))
