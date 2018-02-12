"""
LESSON
-- Line 30: ZeroDivisionError: integer division or modulo by zero
-- [[0,0],[1,1],[0,0]]

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


# Definition for a point.
class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        progress = []
        result =self.check_points(points, 0, progress)
        return result

    def check_points(self, points, pos, progress):
        if pos>=len(points):
            return len(progress)
        p1, p2 = self.get_two_points(progress)
        if not p1 or not p2:
            result = self.check_points(points, pos+1, progress)
            progress.append(points[pos])
            result = max(result, self.check_points(points, pos+1, progress))
            progress.pop()
            return result
        else:
            count=0
            for i in range(pos, len(points)):
                if self.check(p1, p2, points[i]):
                    count+=1
            return count+len(progress)

    def get_two_points(self, points):
        if not points:
            return None, None
        p1 = points[0]
        for p2 in points:
            if p1.x!=p2.x or p1.y!=p2.y:
                return p1, p2
        return p1, None

    def check(self, p1, p2, p):
        if p.x==p1.x and p.y==p1.y or p.x==p2.x and p.y==p2.y:
            return True
        elif p.y==p1.y and p1.y==p2.y:
            return True
        elif p.x == p1.x and p1.x == p2.x:
            return True
        elif (p.y-p1.y)==0 or (p1.y-p2.y)==0:
            return False
        else:
            a=float(p.x-p1.x)/(p.y-p1.y)
            b=float(p1.x-p2.x)/(p1.y-p2.y)
            return a==b


s = Solution()

print s.check(Point(-8,-52), Point(-4,4), Point(-9,-651))
print s.maxPoints([])
print s.maxPoints([Point(0,0)])
print s.maxPoints([Point(0,0), Point(1,1), Point(0,0)])
print s.maxPoints([Point(-4,-4), Point(-8,-582), Point(-3,3), Point(-9,-651), Point(9,591)])
