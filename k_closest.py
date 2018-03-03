"""
--LESSON
-- if key>h[0][0] => if h and key>h[0][0]

https://leetcode.com/problems/find-k-closest-elements/description/
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        return closest(arr, k, x)

import heapq
def closest(arr, k, x):
    h = []
    for a in arr:
        key = get_key(x, a)
        if h and key>h[0][0]:
            if len(h)>=k:
                 heapq.heappop(h)
            heapq.heappush(h, (key, a))
        elif len(h)<k:
            heapq.heappush(h, (key, a))
    result = []
    while h:
        result.append(heapq.heappop(h)[1])
    result.sort()
    return result

def get_key(x, a):
    delta = abs(x-a)
    if a>x:
        delta += 0.5
    return delta * -1

print closest([1,2,3,4,5], 4, 3)