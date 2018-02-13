"""
LESSON
-- missing cache parameter after adding dp
self.reachNumberHelper(start, target+n, n-1, cache)

https://leetcode.com/problems/reach-a-number/description/
You are standing at position 0 on an infinite number line.
There is a goal at position target.

On each move, you can either go left or right.
During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
"""
class Solution(object):
    def reachNumber(self, target):
        n=0
        start=0
        while 1:
            if self.reachNumberHelper(start, target, n, {}):
                return n
            n += 1
        return Raise

    def reachNumberHelper(self, start, target, n, cache):
        if n==0 and start==target:
            return True
        elif n==0:
            return False
        elif n<0:
            return Raise

        cache_key = self.make_key(start, target, n)
        if cache_key in cache:
            return cache[cache_key]

        result = self.reachNumberHelper(start, target+n, n-1, cache) \
                 or self.reachNumberHelper(start, target - n, n - 1, cache)
        cache[self.make_key(start, target, n)] = result
        return result

    def make_key(self, start, target, n):
        key = "{0}.{1}.{2}".format(start, target, n)
        return key

s = Solution()
print s.reachNumber(30)

