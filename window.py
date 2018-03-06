
"""
Given an integer array of size n, find the maximum of the minimums 
of every window size in the array. Note that window size varies from 1 to n.

Example:
Input: 
10 20 30 50 10 70 30
10 20 30

Output: 
70 30 20 10 10 10 10 
30 20 10

Explaination:
Input:  arr[] = {10, 20, 30, 50, 10, 70, 30}
Output:         70, 30, 20, 10, 10, 10, 10

First element in output indicates maximum of minimums of all 
windows of size 1.
Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10},
{70} and {30}.  Maximum of these minimums is 70

Second element in output indicates maximum of minimums of all 
windows of size 2.
Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10},
and {30}.  Maximum of these minimums is 30

Third element in output indicates maximum of minimums of all 
windows of size 3.
Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. 
Maximum of these minimums is 20

Similarly other elements of output are computed.
"""

def window(a):
    if not a:
        return []
    n=len(a)
    for i in range(1, n):
        mval = a[0]
        for j in range(n-i):
            a[j] = min(a[j], a[j+1])
            mval = max(mval, a[j+1])
        a[n-i]=mval
    a.reverse()
    return a

print window([10, 20, 30, 50, 10, 70, 30])

"""
Sliding window min max
Posted on June 1, 2014
Given an array of integer A[] and the size of sliding window w. 
Assume that the window of size w starting from left keeps sliding 
by moving the window one element to right each time. Find the stream 
of sliding minimums in optimal way. A sliding minimum is 
the minimum element of current window.

Lets start with an example for our convenience.

             sliding window                Min         Max
            ---------------               -----       -----
            [1  2  -1] -3  4  2  5  3       -1          2
             1 [2  -1  -3] 4  2  5  3       -3          2
             1  2 [-1  -3  4] 2  6  3       -3          4
             1  2  -1 [-3  4  2] 5  3       -3          4
             1  2  -1  -3 [4  2  5] 3        2          5
             1  2  -1  -3  4 [2  5  3]       2          5
"""
import heapq
class MHeap:
    MIN, MAX = 1, -1
    def __init__(self, key):
        self.heap=[]
        self.key=key
    def push(self, x):
        heapq.heappush(self.heap, x*self.key)
    def peek(self):
        return self.heap[0]*self.key
    def remove(self, x):
        self.heap.remove(x*self.key)
        heapq.heapify(self.heap)

def slide(a, w):
    if not a or not w:
        return []
    n=len(a)
    min_max=[()]*n
    min_heap, max_heap = MHeap(MHeap.MIN), MHeap(MHeap.MAX)
    i,j = 0, 0
    while i<n:
        for k in range(j, min(i+w, n)):
            min_heap.push(a[k])
            max_heap.push(a[k])
            j=k
        min_max[i]=(min_heap.peek(), max_heap.peek())
        min_heap.remove(a[i])
        max_heap.remove(a[i])
        i+=1
        j+=1
    return min_max


print slide([1,  2,  -1, -3,  4,  2,  5,  3 ], 3)

"""
For Example: A = [2,1,3,4,6,3,8,9,10,12,56],  w=4

partition the array in blocks of size w=4. The last block may have less then w.
2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|
Traverse the list from start to end and calculate min_so_far. 
Reset min to 0 after each block (of w elements).
left_min[] = 2, 1, 1, 1 | 6, 3, 3, 3 | 10, 10, 10
Similarly calculate min_in_future by traversing from end to start.
right_min[] = 1, 1, 3, 4 | 3, 3, 8, 9 | 10, 12, 56
now, min at each position i in current window, 
sliding_min(i) = min {right_min[i], left_min[i+w-1]}
sliding_min = 1, 1, 3, 3, 3, 3, 8,
"""

def slide1(a, w):
    n=len(a)
    l, r = [0]*n, [0]*n
    curr=None
    for i in range(n):
        if i%w==0:
            curr = a[i]
            l[i]=a[i]
        else:
            curr = min(curr, a[i])
            l[i] = curr

    for i in range(n-1, -1, -1):
        if i % w == w-1 or i==n-1:
            curr = a[i]
            r[i] = a[i]
        else:
            curr = min(curr, a[i])
            r[i] = curr
    result = [0]*n
    for i in range(n):
        result[i]=min(r[i], l[min(i+w-1, n-1)])
    return result

print slide1([1,  2,  -1, -3,  4,  2,  5,  3 ], 3)

