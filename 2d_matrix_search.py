"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
class Solution(object):
    def searchMatrix(self, m, t):
        if not m or not m[0]:
            return False
        x, y = 0, len(m[0])-1
        while x>=0 and x<len(m) and y>=0 and y<len(m[0]):
            if m[x][y] == t:
                return True
            elif m[x][y]>t:
                y -= 1
            else:
                x += 1
        return False

s = Solution()
print s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]], 5)
