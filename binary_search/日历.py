from sortedcontainers import SortedList
import bisect


class MyCalendar:

    def __init__(self):
        self.booked = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        # print(startTime, endTime, self.booked)
        if len(self.booked) == 0:
            self.booked.add((startTime, -1))
            self.booked.add((endTime-1, 1))
            return True
        else:
            left = bisect.bisect_left(self.booked, startTime, key=lambda x: x[0])
            right = bisect.bisect_right(self.booked, endTime-1, key=lambda x: x[0])

            if right == 0 or left == len(self.booked) or right == left and self.booked[left][1] == -1:
                self.booked.add((startTime, -1))
                self.booked.add((endTime-1, 1))
                return True
            else:
                return False



# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
# ops = ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
# params = [[],[99,100],[45,57],[79,94],[53,72],[88,99],[70,82],[51,69],[84,97],[80,98],[26,44],[73,87],[92,100],[56,74],[50,67],[71,85],[26,41],[96,100],[78,91],[50,61],[27,41],[56,66],[70,80],[82,92],[64,80],[57,76],[13,27],[39,57],[87,100],[92,100],[9,22],[99,100],[31,47],[93,100],[52,65],[53,67],[8,19],[14,26],[42,52],[93,100],[86,100]]

ops = ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
params = [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]


for i in range(1, len(ops)):
    print(obj.book(*params[i]))
# param_1 = obj.book(startTime,endTime)