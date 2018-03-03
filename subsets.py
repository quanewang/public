"""
--LESSON
-- [[]]
"""

def subsets(nums):
    if not nums:
        return [[]]
    result = []
    result1 = subsets(nums[1:])
    result = result + result1
    for x in result1:
        result.append([nums[0]] + x)
    return result

print subsets([1,2,3, 4])