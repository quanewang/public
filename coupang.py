"""
--LESSSON
-- miss checking k<0
"""

"""
k smallest
"""
import heapq
def k_smallest(c, k):
    if not c and not k:
        return []
    if not c or k > len(c):
        raise Exception()
    h = []
    for x in c:
        if len(h) < k:
            heapq.heappush(h, extract(x))
        elif x < heapq.peek(h):
            heapq.heappop(h)
            heapq.heappush(h, extract(x))
    result = []
    while k:
        result.append(heapq.heappop(h)[1])
        k -= 1
    return result

"""
prime between a and b
"""
def extract(x):
    return (x[0] ^ 2 + x[1] ^ 2, x)

def primes(a, b):
  if a<0 or b<0:
      raise Exception("negative input")
  if b<a:
      a, b = b, a
  primes = [2]
  return get_primes(primes, a, b)

def get_primes(primes, a, b):
    result = []
    current = primes[-1]+1
    while current<=b:
        is_prime = True
        for x in primes:
            if current % x == 0:
                is_prime=False
                break
        if is_prime:
            primes.append(current)
            if current in range(a, b+1):
                result.add(current)
        current += 1
    return result



