"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
"""
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return None
    if matrix[0][0]>target or matrix[-1][-1]<target:
        return None
    row = find_row(matrix, target)
    if row == None:
        return None
    return row, search(matrix[row], target)

def find_row(m, t):
    low = 0
    high = len(m) - 1
    while low<high:
        mid = (low+high)/2
        if t in range(m[mid][0], m[mid][-1]+1):
            return mid
        elif m[mid][-1]<t:
            low = mid + 1
        else:
            high = mid - 1
    if t in range(m[low][0], m[low][-1]+1):
        return low
    return None

def search(m, x):
    low = 0
    high = len(m) - 1
    while low<high:
        mid = (low+high)/2
        if x == m[mid]:
            return mid
        elif m[mid]<x:
            low = mid + 1
        else:
            high = mid - 1
    if x == m[low]:
        return low
    return None

print searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 50)