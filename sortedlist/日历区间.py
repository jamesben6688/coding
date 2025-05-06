from sortedcontainers.sortedlist import SortedList
import bisect


class MyCalendar:

    def __init__(self):
        self.booked = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        index = bisect.bisect_left(self.booked, endTime, key=lambda x: x[0])

        if index == 0 or self.booked[index-1][1] <= startTime:
            self.booked.add([startTime, endTime])
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
ops=["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
params = [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
obj = MyCalendar()
for i in range(1, len(ops)):
    print(obj.book(*params[i]))
# param_1 = obj.book(startTime,endTime)
