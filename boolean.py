"""
Given a boolean expression with following symbols.

Symbols
    'T' ---> true
    'F' ---> false

And following operators filled between symbols

Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR

Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

For Example:
The expression is "T | T & F ^ T", it evaluates true
in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T)
and (T|((T&F)^T)).

Input:
T|T&F^T
T^F|F
Output:
4
2
"""
def p(stmt):
    symbols, ops = [], []
    for x in stmt:
        if x in ['T', 'F']:
            symbols.append(x)
        else:
            ops.append(x)

    count = phelper(symbols, ops, 0, len(symbols) - 1, True,  {})
    return count

def key(i, j, b):
    return '{}.{}.{}'.format(i, j, b)

def phelper(symbols, ops, i, j, b, mem):
    if not symbols or not ops:
        return 0
    if key(i, j, b) in mem:
        return mem[key(i, j, b)]
    if i==j:
        if symbols[i]=='T':
            mem[key(i, j, True)] = 1
            mem[key(i, j, False)] = 0
        else:
            mem[key(i, j, True)] = 0
            mem[key(i, j, False)] = 1
        return mem[key(i, j, b)]
    count = 0
    for k in range(i, j):
        if ops[k] == '|':
            if b:
                count += phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, True, mem) \
                         + phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, True, mem) \
                         + phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, False, mem)
            else:
                count += phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, False, mem)
        elif ops[k] == '&':
            if b:
                count += phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, True, mem)
            else:
                count += phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, False, mem) \
                         + phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, True, mem) \
                         + phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, False, mem)
        else:
            if b:
                count += phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, False, mem) \
                         + phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, True, mem)
            else:
                count += phelper(symbols, ops, i, k, True, mem) * phelper(symbols, ops, k + 1, j, True, mem) \
                         + phelper(symbols, ops, i, k, False, mem) * phelper(symbols, ops, k + 1, j, False, mem)
    mem[key(i, j, b)]=count
    return count


print p("T|T&F^T")
print p("T^F|F")

