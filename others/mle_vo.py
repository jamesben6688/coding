"""
https://www.1point3acres.com/bbs/thread-1113179-1-1.html
coding1.1:
给定一个包含多个人的 24 小时工作安排表，每个人都有姓名、班次开始时间和结束时间.
编写一个函数，输入该工作安排表和一个时间，然后返回在该时间工作的员工人数。
coding1.2:
编写一个函数，接收一个工作安排表，并返回一张不包含重叠时段的时间表，说明在每个时间段内谁在工作。
返回一个列表，其中的每个元素也是一个列表，包含“开始时间”、“结束时间”以及在该时间段内工作的人员列表。
"""

from typing import List, Tuple


def count_employees_working_at_time(schedule: List[Tuple[str, int, int]], given_time: int) -> int:
    """
    计算给定时间有多少员工正在工作

    :param schedule: 员工的工作时间表，每个员工由姓名、开始时间和结束时间表示
    :param given_time: 给定时间，24小时制整数
    :return: 在该时间工作的员工人数
    """
    count = 0

    for name, start_time, end_time in schedule:
        # 检查给定时间是否在员工的工作时间范围内
        if start_time <= given_time < end_time:
            count += 1

    return count


# 示例
schedule = [
    ("Alice", 9, 17),  # Alice 9:00-17:00
    ("Bob", 8, 16),  # Bob 8:00-16:00
    ("Charlie", 13, 21),  # Charlie 13:00-21:00
    ("David", 12, 18)  # David 12:00-18:00
]

given_time = 15  # 查询 15:00 时在工作的人数
print(count_employees_working_at_time(schedule, given_time))  # 输出 4


