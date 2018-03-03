import os

def rotate(arr):
    low, high = 0, len(arr)-1
    if arr[low]<arr[high]:
        return low
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=arr[0]:
            low = mid+1
        else:
            high = mid-1
    return low

print rotate([9, 1])
import heapq
def maxheap_push(h, x):
    heapq.heappush(h, x*-1)

def maxheap_pop(h):
    return heapq.heappop(h)*-1

a = []
maxheap_push(a, 3)
maxheap_push(a, 1)
maxheap_push(a, 5)
print a
print maxheap_pop(a)
print maxheap_pop(a)
print maxheap_pop(a)

