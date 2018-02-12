"""
LESSON
- []
- [1] => []
- arr[i] = 1 if i==0
- arr[i] = left[i - 1] if i>0
- arr[i] = arr[i] * compute(arr, right, i + 1)
- left and right cache

Given an array of integers arr, youre asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solutions time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] #
"""

def array_of_array_products(arr):
    if not arr:
        return arr
    if len(arr) == 1:
        return []
    left = {}
    right = {}
    for i in range(0, len(arr)):

        if i == 0:
            left[i] = arr[i]
            arr[i] = 1
        else:
            left[i] = left[i - 1] * arr[i]
            arr[i] = left[i - 1]
        arr[i] = arr[i] * compute(arr, right, i + 1)
    return arr

def compute(arr, right, i):
    if i>len(arr)-1:
        return 1
    if i in right:
        return right[i]
    result = arr[i] * compute(arr, right, i+1)
    right[i]=result
    return result


arr = [2, 7, 3, 4]
print array_of_array_products(arr)
print array_of_array_products([])
print array_of_array_products([2])