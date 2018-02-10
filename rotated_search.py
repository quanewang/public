# Question 6: Given a Sorted Array which has been rotated,
# write the code to find a given Integer

# LESSON
# - logic helper functions: is_mixed_range, is_mid_in_larger_group
# - high = len(nums) => high = len(nums)-1
# - binary search high = mid-1
# - binary search low = mid+1
# - [6, 7] low=0 mid=0 high=1, search for 7
# low<high ==> low<=high

def find(nums, key):
    if not nums or not key:
        return -1
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)/2
        if nums[mid] == key:
            return mid
        if low==high:
            return -1
        if is_mixed_range(nums, low, high):
            if is_mid_in_larger_group(nums, low, mid, high):
                if nums[mid]>key:
                    if nums[high]>=key:
                        low = mid+1
                    else:
                        high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]>key:
                    high = mid-1
                else:
                    if nums[high]>=key:
                        low=mid+1
                    else:
                        high=mid-1
        else:
            if nums[mid]>key:
                high=mid-1
            else:
                low = mid+1
    return -1

#to do duplicates?
def is_mixed_range(nums, low, high):
    return nums[low]>nums[high]

def is_mid_in_larger_group(nums, low, mid, high):
    return nums[mid]>nums[high]

nums = [5, 6, 7, 8, 1, 2, 3, 4]
print find(nums, 7)
print find(nums, 1)
print find(nums, 8)
print find(nums, 5)
print find(nums, 4)
print find(nums, 9)