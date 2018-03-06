"""
LESSON
-- base += base + ... => base += ...

Find the nth digit of the infinite integer sequence
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
which is part of the number 10.
"""

def nth(n):
    i=1
    while n>=9*pow(10, i-1)*i:
        n -= 9*pow(10, i-1)*i
        i+=1
    x = n//i+pow(10, i-1)-1
    if n%i==0:
        return str(x)[-1]
    else:
        return str(x+1)[n%i-1]
    return x[n%i]

print nth(22)

class Solution:
    def findNthDigit(self, n):
        if not n:
            return None
        if n <= 9:
            return n
        i = 1
        base = 0
        while base + 9 * pow(10, i - 1) * i < n:
            base += 9 * pow(10, i - 1) * i
            i = i + 1
        i = i
        n = n - base
        num = n / i
        if n % i == 0:
            return int(str(num + pow(10, i - 1) - 1)[-1])
        else:
            return int(str(num + pow(10, i - 1))[n % i - 1])

s=Solution()
#print s.findNthDigit(11) #0
#print s.findNthDigit(18) #1
#print s.findNthDigit(10000) #7
