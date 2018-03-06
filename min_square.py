"""
Given a paper of size A x B. Task is to cut the paper into
squares of any size. Find the minimum number
of squares that can be cut from the paper.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case contains two integer
A and B denoting the two size of the paper.

Output:
Print the minimum number of squares that can be cut from the paper.

13 29: 9

30 35: 5
15 20
"""

def min_square(a, b):
    return min_square_help(a, b, {})

def min_square_help(a, b, mem):
    if not a or not b:
        return 0
    if a == b:
        return 1
    if key(a, b) in mem:
        #print key(a, b), mem[key(a, b)]
        return mem[key(a, b)]
    a, b = min(a, b), max(a, b)
    count = a*b
    #print a, b, mem, count
    for i in range(1, a+1):
        current = min_square_help (a-i, b, mem) + min_square_help(i, b-i, mem)
        if current<count:
            count = current + 1
        current = min_square_help (a, b-i, mem) + min_square_help(i, a-i, mem)
        if current < count:
            count = current + 1
    mem[key(a, b)] = count
    return count

def key(a, b):
    return a*100 + b

print min_square(13, 29)
print min_square(30, 35)
