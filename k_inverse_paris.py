"""
Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation:
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
Example 2:
Input: n = 3, k = 1
Output: 2
Explanation:
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

https://leetcode.com/problems/k-inverse-pairs-array/description/
"""
class Solution(object):
    def kInversePairs(self, n, k):
        return kInverse([], range(1, n+1), 0, k)

def kInverse(left, right, cur_k, k):
    if cur_k==k:
        return 1
    elif cur_k>k:
        return 0
    elif not right:
        return 0
    count = 0
    for i in range(0, len(right)):
        left.append(right[i])
        right.pop(i)
        count += kInverse(left, right, cur_k + i, k)
        right_i = left.pop()
        right.insert(i, right_i)
    return count

s = Solution()
print s.kInversePairs(10,13)