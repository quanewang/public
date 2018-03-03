"""
https://leetcode.com/problems/my-calendar-iii/description/
"""
import bisect
class MyCalendarThree(object):
    def __init__(self):
        self.n = []
        self.k = 0

    def book(self, start, end):
        START = 1
        END = 0
        bisect.insort(self.n, (start, START))
        bisect.insort(self.n, (end, END))
        count = 0
        for x in self.n:
            if x[1] == START:
                count += 1
                self.k = max(count + 1, self.k)
            else:
                count -= 1
        return self.k


obj = MyCalendarThree()
l = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
for x in l:
    print obj.book(x[0], x[1])
