"""
Given a non-empty 2D matrix matrix and an integer k,
find the max sum of a rectangle in the matrix
such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83597/Java-Binary-Search-solution-time-complexity-min(mn)2*max(mn)*log(max(mn))
"""


def maxSumSubmatrix(matrix, k):
    if not matrix:
        return None
    h = len(matrix)
    w = len(matrix[0])
    if h==0 or w==0:
        return None
    max_sum = 0
    for i in range(w):
        for j in range(i, w):
            sums=[]
            row_sum = 0
            for x in range(h):
                for y in range(i, j+1):
                    row_sum += matrix[x][y]
                if row_sum==k:
                    return k
                elif max_sum<row_sum and row_sum<k:
                    max_sum = row_sum
                ceiling = find_ceiling(sums, row_sum - k)
                if ceiling is not None and ceiling == (row_sum - k):
                    return k
                elif ceiling is not None and (row_sum - ceiling) > max_sum:
                    max_sum = row_sum - ceiling
                sums.append(row_sum)
    return max_sum

def find_ceiling(sums, n):
    if not sums:
        return None
    sums = list(sums)
    sums.sort()
    if sums[-1]<n:
        return None
    low = 0
    high = len(sums)-1
    while low<=high:
        mid = (low + high)/2
        if sums[mid] == n:
            return n
        if low == high:
            if sums[low]<n:
                while low<len(sums) and sums[low]<n:
                    low += 1
                if low>=len(sums):
                    return None
            return sums[low]
        if sums[mid]>n:
            high = mid - 1
        else:
            low = mid + 1
    return None


matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
print maxSumSubmatrix(matrix, 5)