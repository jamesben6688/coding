class Cake:
    def __init__(self, x, y, width, height):
        self.x = x  # 蛋糕的x坐标
        self.y = y  # 蛋糕的y坐标
        self.width = width  # 蛋糕的宽度
        self.height = height  # 蛋糕的高度


def get_area_below_line(cake, l):
    delta_line = l-cake.y
    if delta_line > cake.height:
        return cake.width * cake.height
    elif delta_line < 0:
        return 0
    else:
        return cake.width * (l-cake.y)

def find_cut_line(cakes):
    # 计算所有蛋糕的总面积
    total_area = sum(cake.width * cake.height for cake in cakes)

    bottom_line = float('inf')
    top_line = -float('inf')

    total_area = 0
    for cake in cakes:
        bottom_line = min(bottom_line, cake.y)
        top_line = max(top_line, cake.y+cake.height)
        total_area += cake.height * cake.width

    l = bottom_line
    r = top_line

    while l < r:
        mid = l + (r-l) / 2
        area_sum = 0
        for cake in cakes:
            area_sum += get_area_below_line(cake, mid)

        if abs(area_sum*2-total_area) < 1e-6:
            return mid
        elif area_sum*2 > total_area:
            r = mid
        else:
            l = mid

    return None


# 示例使用
cakes = [
    (0, 0, 5, 10),  # 蛋糕1：左下角(0,0)，宽5高10
    (0, 10, 6, 12),  # 蛋糕2：左下角(0,10)，宽6高12
    (6, 5, 4, 8)     # 蛋糕3：左下角(5,5)，宽4高8
]

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.xlim(left=0, right=20)
plt.ylim(top=20, bottom=0)
#
for x, y, w, h in cakes:
    rect = mpatches.Rectangle((x, y), w, h,
                              fill=False,
                              color="red",
                              linewidth=2)
    # facecolor="red")
    plt.gca().add_patch(rect)


# rect = mpatches.Rectangle((0, 0), 2, 3,
#                               fill=True,
#                               color="red",
#                               linewidth=1)
# facecolor="red")
# plt.gca().add_patch(rect)


cakes = [Cake(*x) for x in cakes]
cutting_line = find_cut_line(cakes)
print(f"The cutting line is at y = {cutting_line}")

plt.axhline(y=cutting_line, color='g', linestyle='--', linewidth=2)

plt.show()
