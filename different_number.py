"""
Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function
getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Solve first for the case when youre NOT allowed to modify the input arr.
If successful and still have time, see if you can come up with an algorithm with
an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4
"""

def getDifferentNumber(arr):
    if not arr:
        return 0
    i = 0
    while i<len(arr):
        if arr[i]!=-1:
            if arr[i] in range(len(arr)):
                if arr[i] != i:
                    tmp = arr[arr[i]]
                    arr[arr[i]] = arr[i]
                    arr[i] = tmp
                    continue
            else:
                arr[i] = -1
        i += 1

    for i in range(len(arr)):
        if arr[i]==-1:
            return i
    return len(arr)

print getDifferentNumber([2, 4, 9, 0, 1])