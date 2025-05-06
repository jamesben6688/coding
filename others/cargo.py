from heapq import heappop, heappush


def process_goods(d, k):
    waiting_area = []

    while True:
        # 接收一个新货物
        new_goods = input("请输入新货物：")
        if new_goods == "":  # 如果没有输入，结束循环
            break

        new_goods = int(new_goods)

        # 将新货物加入到等待区
        # heappush(waiting_area, new_goods)
        waiting_area.append(new_goods)

        # 判断是否能组成一个合法的包
        if len(waiting_area) >= k:
            # 取出所有货物的排列组合，进行判断
            waiting_area.sort()  # 对货物进行排序

            for i in range(len(waiting_area) - k + 1):
                selected_goods = waiting_area[i:i + k]
                if selected_goods[-1] - selected_goods[0] <= d:
                    # 满足条件，输出并移除这 k 个货物
                    print(selected_goods[0], selected_goods[1], selected_goods[2])
                    # 移除已经打包的 k 个货物
                    del waiting_area[i:i + k]
                    break


process_goods(3, 3)


# class Solution:
#     def package(self, input_stream, d, k):
#         left = 0
#         right = k-1
#         n = len(input_stream)
#         ans = []
#
#         while right < n:
#             if right - left + 1 >= k:
#                 mx_gap = -1
#                 for i in range(left+1, right+1):
#                     mx_gap = max(mx_gap, input_stream[i]-input_stream[i-1])
#                     if mx_gap > d:
#                         break
#
#                 if mx_gap <= d:
#                     ans.append(input_stream[left:right+1])
#                     left = right + 1
#             right += 1
#         return ans
#
#
# print(Solution().package([1, 4, 5, 7, 8, 9, 22], d=3, k=3))
