"""
https://leetcode.com/problems/summary-ranges/description/
"""
class Solution(object):
    def summaryRanges(self, nums):
        return summary(nums)

def summary(nums):
    if not nums:
        return []
    result = []
    prev = nums[0]
    start=prev
    for x in nums[1:]:
        if x!=prev+1:
            result.append(make(start, prev))
            start = x
        prev = x
    result.append(make(start, prev))
    return result

def make(x, y):
    if x==y:
        return str(x)
    return str(x) + "->" + str(y)