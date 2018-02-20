"""
A sequence of numbers is called arithmetic if it consists of
at least three elements and if the difference between
any two consecutive elements is the same.
For example, these are arithmetic sequences:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.
1, 1, 2, 5, 7
Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""

def numberOfArithmeticSlices(A):
    print slices(A, 0, [])

def slices(A, idx, progress):
    result = 0
    if not A:
        return result
    if idx==len(A):
        if len(progress)>2:
            print progress
        return 1 if len(progress)>2 else 0
    if is_compatible(progress, A[idx]):
        progress.append(A[idx])
        result += slices(A, idx + 1, progress)
        progress.pop()
    result += slices(A, idx + 1, progress)
    return result

def is_compatible(progress, element):
    if not progress or len(progress)<2:
        return True
    return element-progress[-1] == progress[-1] - progress[-2]


numberOfArithmeticSlices([2, 4, 6, 8, 10])


