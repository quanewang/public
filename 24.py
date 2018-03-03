"""
https://leetcode.com/problems/24-game/description/
"""

class Solution(object):
    def judgePoint24(self, nums):
        numss = permutate(nums)
        #print numss
        for n in numss:
            result = compute(n)
            for x in result:
                if abs(x-24)<0.001:
                    return True
        return False

def permutate(nums):
    result = []
    if len(nums)==1:
        return [list(nums)]
    for i in range(0, len(nums)):
        nums_i = nums[i]
        nums_others = nums[:i] + nums[i+1:]
        permuted = permutate(nums_others)
        for x in permuted:
            e = [nums_i] + x
            result.append(e)
    return result

def compute(nums):
    if not nums:
        return [0]
    if len(nums)==1:
        return [nums[0]]
    result = []
    for i in range(1, len(nums)):
        a = compute(nums[:i])
        b = compute(nums[i:])
        for x in a:
            for y in b:
                result.append(x+y)
                result.append(x-y)
                result.append(x*y)
                if y:
                    result.append(float(x)/float(y))
    return result

s = Solution()
#print s.judgePoint24([1,3,4,6])

#print s.judgePoint24([1,1,7,7])
print s.judgePoint24([3,3,8,8])