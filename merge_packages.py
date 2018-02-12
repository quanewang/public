"""
LESSON
-- for idx, value in enumerate(arr)
-- h[i]=arr[i] => for h[v]=i
-- 21 => limit

Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1]
"""


def get_indices_of_item_wights(arr, limit):
    if arr is None:
        return []
    h = {}
    for i, v in enumerate(arr):
        if limit - v in h:
            return [i, h[limit - v]]
        h[v] = i
    return []
