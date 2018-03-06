'''
LESSON
- missing mid = (low+high)/2
- high = len(arr-1) => high = len(arr)-1

Array Index & Element Equality
Given a sorted array arr of distinct integers,
write a function indexEqualsValueSearch that
returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index.
Analyze the time and space complexities of your
solution and explain its correctness.
'''



def index_equals_value_search(arr):
  low = 0
  high = len(arr)-1
  mid = 0
  while(low<=high):
    mid = (low+high)/2
    if arr[mid]==mid:
      return mid
    elif arr[mid]>mid:
      high = mid - 1
    else:
      low = mid  + 1
  return -1

arr = [-8,0,2,5]
arr1 = [-1,0,3,6]
print index_equals_value_search(arr)