"""
--LESSON
-- n/2==0 => n%2==0

There is a list of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left,
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left,
until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

def lastRemaining(n):
    return lastRemaningRecursive(n, True)

def lastRemaningRecursive(n, isLeft):
    if n==1:
        return 1
    if isLeft:
        return lastRemaningRecursive(n/2, False) * 2
    elif n%2==0:
        return lastRemaningRecursive(n/2, True) * 2 - 1
    else:
        return lastRemaningRecursive(n/2, True) * 2

print lastRemaining(9)