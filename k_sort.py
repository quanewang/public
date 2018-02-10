'''
HEAP
K
'''

import heapq

def sort(arr, k):
    if not k:
        return arr
    result = []
    h = []
    for x in arr:
        if len(h)==k:
            result.append(heapq.heappop(h))
        heapq.heappush(h, x)
    while len(h)>0:
        result.append(heapq.heappop(h))
    return result

print sort([0, 4, 2, 3, 5, 7, 6], 2)