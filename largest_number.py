"""
LESSON
-- return ''.join(nums) => return ''.join(result)
-- [0, 0] => "00" => "0"

Largest Number
DescriptionHintsSubmissionsDiscussSolution
Pick One
Given a list of non negative integers, arrange them such that
they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string
instead of an integer.
"""

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        result = []
        for num in nums:
            inserted = False
            for i in range(len(result)):
                if int(str(num)+result[i])>=int(result[i]+str(num)):
                    result.insert(i, str(num))
                    inserted = True
                    break
            if not inserted:
                result.append(str(num))
        return self.strip(''.join(result))

    def strip(self, s):
        while s[:2]=="00":
            s = s[1:]
        return s

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])
print s.largestNumber([0,0])


