"""
Total Hamming Distance
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
"""

def hamming(m, n):
    if m>n:
        m, n = n, m
    count = 0
    while m>0:
        count += 1 if m%2!=n%2 else 0
        m /= 2
        n /= 2

    while n>0:
        n /=2
        count += 1
    return count

print hamming(4, 14)
print hamming(4, 2)
print hamming(2, 14)