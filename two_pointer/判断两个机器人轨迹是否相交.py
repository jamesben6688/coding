class Robot:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.cur_dir = 1
        """
            |(0)
       (3) - - (1)
            |(2)
        
        """
        self.dir_map = {
            0: (-1, 0),
            1: (0, 1),
            2: (1, 0),
            3: (0, -1)
        }

    def step(self, action):
        """
            F for forward, L for turn left, R for turn right
        :param action:
        :return:
        """
        if action == 'L':
            self.cur_dir = (self.cur_dir + 3) % 4
        elif action == 'R':
            self.cur_dir = (self.cur_dir + 1) % 4
        else:
            self.start_x += self.dir_map[self.cur_dir][0]
            self.start_y += self.dir_map[self.cur_dir][1]

        return (self.start_x, self.start_y)


class Solution:
    def robot_intersect(self, start1, dir1, start2, dir2):

        robot1 = Robot(*start1)
        robot2 = Robot(*start2)

        d1 = dir1
        d2 = dir2
        pt1 = start1
        pt2 = start2

        i = 0
        j = 0
        while pt1 != pt2:
            if i < len(dir1):
                pt1 = robot1.step(dir1[i])
                i += 1
            elif i == len(dir1):
                pt1 = (-1, -1)
            else:
                i = 0
                pt1 = start2
                dir1 = d2
                robot1 = Robot(*start2)

            if j < len(dir2):
                pt2 = robot2.step(dir2[j])
                j += 1
            elif j == len(dir2):
                pt2 = (-1, -1)
            else:
                j = 0
                pt2 = start1
                dir2 = d1
                robot2 = Robot(*start1)
            print(f"pt1: {pt1}, pt2: {pt2}")
        print(pt1)
        return pt1 != (-1, -1)


print(Solution().robot_intersect(
    start1=(0, 0), dir1="FFRFFF",
    start2=(1, 0), dir2="RFFLFF"
))

"""
robot1 = "FFRFFR"
robot2 = "RFFLFF"
# 机器人1路径: (0,0)->(0,1)->(0,2)->(0,2)->(1,2)->(2, 2)->(3, 2)
# 机器人2路径: (1,0)->(1,0)->(2,0)->(3,0)->(3,0)->(3, 1)->(3, 2)
# ✅ 交点: (2,2)
"""
