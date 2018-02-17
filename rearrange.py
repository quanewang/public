"""
Rearrange an array with O(1) extra space
Given an array arr[] of size n where every element is in range from 0 to n-1.
Rearrange the given array so that arr[i] becomes arr[arr[i]].
This should be done with O(1) extra space.

Input:
1 0
4 0 2 1 3
3 2 0 1

Output:

0 1
3 4 2 0 1
1 0 3 2

i=0
i=4

i=0
while
tmp_i=0
tmp_arr_i=4
arr[0]=arr[arr[0]]=3
arr_i=4

tmp_i=1
tmp_arr_i=0
arr[1]=arr[arr[1]]=4
i=1
arr_i=0

tmp_i=3
tmp_arr_i=1
arr[3]=arr[arr[3]]=0
i=3
arr_i=1

tmp_i=4
tmp_arr_i=3
arr[4]=arr[arr[4]]=1
i=4
arr_i=3
"""
def rearrange(arr):
    if not arr:
        return arr
    count = 0
    done = []
    for i in range(len(arr)):
        v = None
        while count < len(arr) and i != None:
            if i not in done:
                done.append(i)
                if v == None:
                    v = arr[arr[i]]
                v, arr[i] = arr[i], v
                i = find(arr, i, done)
                count += 1
            else:
                break
    return arr

def find(arr, v, done):
    for i in range(len(arr)):
        if arr[i]==v and i not in done:
            return i
    return None

print rearrange([4, 0, 2, 1, 3])
print rearrange([3, 2, 0, 1])
print rearrange([1,0])
