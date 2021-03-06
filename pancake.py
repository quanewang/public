"""
LESSON
-- boundary

He should communicate more. Preferably constantly during the interview.
Silence is not a good thing here. It's difficult for the interviewer
to know what you're thinking or if you're going down the wrong path
if you don't think out loud. His code can be more Pythonic/idiomatic.
In Python, we can swap values with a single line "arr[i], arr[j] = arr[j], arr[i]".
There's no need for a temp variable. Pay extra attention and look for
off by 1 errors when dealing with 0-based and 1-based values.


Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output


"""

def pancake_sort(arr):
    if not arr:
        return arr
    counter = len(arr)
    while counter > 1:
        k = find_largest(arr, counter-1)
        flip(arr, k + 1)
        flip(arr, counter)
        counter -= 1
    return arr


def find_largest(arr, boundary):
    pos = 0
    for i in range(0, boundary + 1):
        if arr[pos] < arr[i]:
            pos = i
    return pos


def flip(arr, k):
    low = 0
    high = k - 1
    while low < high:
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
        low += 1
        high -= 1


print pancake_sort([5, 4, 3, 2, 1])