# Write a function
# for finding the index of the "rotation point,"
# which is where I started working from the beginning
# of the dictionary.This list is huge (there are
# lots of words I don't know) so we want to be
# efficient here.



def find(words):
    if not words:
        return None
    low = 0
    high = len(words)-1
    while low<high-1:
        mid = (low + high)/2
        if words[mid]>words[high]:
            if words[mid]<words[mid+1]:
                low = mid+1
            else:
                return mid+1
        else:
            if words[mid]<words[mid-1]:
                return mid
            else:
                high = mid-1
    if low==high-1:
       if words[low]>words[high]:
           return high
       else:
           return low
    if low==high:
        return high
    return None


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print find(words)

print find([1, 2, 3, 4, 5])

print find([1, 2, 3, 4, 5, 0])

print find([1, 2])
print find([1])
print find([2, 1])


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