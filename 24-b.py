class Solution(object):
    def judgePoint24(self, nums):
        result = compute(nums)
        for x in result:
            if abs(x - 24) < 0.001:
                return True
        return False

def compute(nums):
    result = []
    if not nums:
        return result
    if len(nums)==1:
        return [nums[0]]
    subs = subsets(nums)
    for sub1 in subs:
        if not sub1 or len(sub1)==len(nums):
            continue
        sub2 = counterpart(nums, sub1)
        if not sub2:
            continue
        l = compute(sub1)
        r = compute(sub2)
        for x in l:
            for y in r:
                result.append(x*y)
                if y:
                    result.append(float(x)/float(y))
                result.append(x-y)
                result.append(x+y)
    return result

def subsets(nums):
    if not nums:
        return [[]]
    result = []
    result1 = subsets(nums[1:])
    result = result + result1
    for x in result1:
        result.append([nums[0]] + x)
    return result

def counterpart(nums, subset):
    result = list(nums)
    for n in subset:
        result.pop(result.index(n))
    return result

s = Solution()
print s.judgePoint24([8,1,6,6])
print s.judgePoint24([1,3,4,6])
print s.judgePoint24([3,3,8,8])