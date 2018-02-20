"""
Find Prime numbers in a range
Generate all prime numbers between two given numbers.
For every test case print all prime numbers p such that m <= p <= n, space separated.
Example:
Input:
1 10
3 5
Output:
2 3 5 7
3 5
"""
def prime(low, high):
    if low>high:
        return []
    primes = []
    result = []
    for n in range(2, high+1):
        is_prime = True
        for p in primes:
            if n%p==0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            if n >= low:
                result.append(n)
    print result

prime(1, 10)
