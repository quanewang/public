'''
Given integers n and k, find the lexicographically k-th smallest integer
in the range from 1 to n.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
so the second smallest number is 10.
'''

class Solution(object):
    def findKthNumber(self, n, k):
        cur = 1
        k = k - 1
        while k>0 and cur < n:
            steps = self.count_steps(cur, cur + 1, n)
            if k < steps:
                cur = cur * 10
                k = k - 1
            else:
                k = k - steps
                cur += 1
        return cur

    def count_steps(self, n1, n2, n):
        steps = 0
        while n1*10<=n:
            steps += n2 - n1
            n1 = n1 * 10
            n2 = n2 * 10
        steps = min(steps + n-n1+1, steps + n2 - n1)

        return steps


s = Solution()
#print s.count_steps(1, 2, 10)
#print s.count_steps(10, 11, 14)
print s.findKthNumber(13, 2) # expect 10
print s.findKthNumber(10, 3) # expect 2
print s.findKthNumber(1000, 31)