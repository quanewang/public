"""
https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

def rotate(m):
    n = len(m)
    for l in range(n/2):
        for y in range(l, n-l-1):
            tmp = m[l][y]
            m[y][n-l-1], tmp = tmp, m[y][n-l-1]
            m[n-l-1][n-y-1], tmp = tmp, m[n-l-1][n-y-1]
            m[n-y-1][l], tmp = tmp, m[n-y-1][l]
            m[l][y], tmp = tmp, m[l][y]
    print m

rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])

