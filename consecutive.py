"""
--LESSON
--  if possible(seq2): => if not seq2 or possible(seq2):

https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
"""

class Solution(object):
    def isPossible(self, nums):
        return possible(nums)

def possible(nums):
    seqs = sequences(nums, [])
    for seq1 in seqs:
        seq2 = counterpart(nums, seq1)
        if not seq2 or possible(seq2):
            return True
    return False

def sequences(nums, progress):
    if not nums:
        if len(progress)>2:
            return [list(progress)]
        return []
    result = []
    if not progress or progress[-1]+1==nums[0]:
        progress.append(nums[0])
        result += sequences(nums[1:], progress)
        progress.pop()
    result += sequences(nums[1:], progress)
    return result

def counterpart(nums, subset):
    result = list(nums)
    for n in subset:
        result.pop(result.index(n))
    return result

s = Solution()
print s.isPossible([1,2,3,3,4,5])