# Question 7: You have a number of incoming Integers,
# all of which cannot be stored into memory.
# We need to print largest K numbers at the end of input

import heapq
def largest_k(nums, k):
    heap = []
    for num in nums:
        if len(heap)>=k:
            heapq.heappop(heap)
        heapq.heappush(heap, num)
    print heap

largest_k([9,2,4,1,0,5,6], 4)

'''
- use priority queue for skyline heap
'''