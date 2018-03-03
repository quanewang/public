"""
football scoring 2, 3, 6, 6+1, 6+2
"""
def football(n):
    return score_rec(n, {})

def score_rec(n, memo):
    points=[2, 3, 6, 7, 8]
    if n==0:
        return 1
    elif n<0:
        return 0
    if n in memo:
        return memo[n]
    result = 0
    for x in points:
        result += score_rec(n-x, points, memo)
    memo[n] = result
    return result

def score_dp(n):
    points=[2, 3, 6, 7, 8]
    memo = [0]*(n+1)
    memo[0]=1
    memo[1]=0
    for i in range(2, n+1):
        for x in points:
            memo[i] += get_memo(memo, i - x)
    return memo[n]

def get_memo(memo, i):
    return 0 if i<0 else memo[i]

print score_dp(10)


def stair_dp(n):
    steps=[1, 2]
    memo = [0]*(n+1)
    memo[0]=1
    for i in range(1, n+1):
        for x in steps:
            memo[i] += get_memo(memo, i - x)
    return memo[n]

def get_memo(memo, i):
    return 0 if i<0 else memo[i]

print stair_dp(10)

