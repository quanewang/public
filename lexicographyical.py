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

log(n)
15670
1xxxx 5670
1xxx 10^3
1xx  10^2
1x   10^1

15670
15xxx 670
13xxx 10^3
13xx  10^2
13x   10^1

[1,3]
13000
[1,4]
14000
'''

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        p = 1
        while p <= n and k>0:
            count = self.count(n, p)
            print n, p, count, k
            if count == k:
                return p
            if count > k:
                p = p * 10
                k -= 1
            else:
                p = p + 1
                k = k - count
        return p


    # n=189, p=13
    def count(self, n, p):
        """
        :param n: 189
        :param prefix: [1, 3]
        :return:
        """
        num = self.split(n)
        prefix = self.split(p)
        if len(num)==len(prefix) and num>=prefix:
            return 1
        elif len(num)==len(prefix):
            return 0
        zeros = pow(10, len(num) - len(prefix))
        prefix_plus = self.inc(prefix)
        if self.to_num(prefix_plus)*zeros<n:
            count = zeros
        else:
            count = n-self.to_num(prefix)*(zeros)+1
        #print zeros, count, prefix_plus, self.to_num(prefix_plus)*zeros<n, n
        for i in range(0, len(num)-len(prefix)):
            count += pow(10, i)
        return count

    # n=189, p=13
    def verifyNumberWithPrefix(self, n, p):
        count=0
        for i in range(n+1):
            if str(i).startswith(str(p)):
                count += 1
        return count


    def to_num(self, list):
        num = 0
        for x in list:
            num = num * 10 + x
        return num

    def split(self, n):
        result = []
        while n>0:
            result.append(n % 10)
            n = n/10
        result.reverse()
        return result
    def inc(self, n):
        #todo carry
        plus = []+n
        plus[len(n)-1] = plus[len(n)-1] + 1
        return plus


s = Solution()
print s.count(13, 1)
print s.findKthNumber(13, 2)
print s.findKthNumber(10, 3)