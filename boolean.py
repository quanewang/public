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
def p1(stmt):
    if not stmt:
        return 0
    print phelper1(stmt, 0, len(stmt)-1, True)

def phelper1(stmt, low, high, b):
    if low>high:
        return 0
    if low==high:
        if stmt[low] == 'T':
            return 1 if b else 0
        else:
            return 0 if b else 1
    count = 0
    for k in range(low+1, high, 2):
        if stmt[k] == '&' and b:
            count += phelper1(stmt, low, k-1, b) * phelper1(stmt, k+1, high, b)
        elif stmt[k] == '&' and not b:
            count += phelper1(stmt, low, k-1, True) * phelper1(stmt, k+1, high, False) \
                     + phelper1(stmt, low, k-1, False) * phelper1(stmt, k+1, high, True)\
                     + phelper1(stmt, low, k - 1, False) * phelper1(stmt, k + 1, high, False)
        elif stmt[k] == '|' and b:
            count += phelper1(stmt, low, k - 1, True) * phelper1(stmt, k + 1, high, False) \
                     + phelper1(stmt, low, k - 1, False) * phelper1(stmt, k + 1, high, True) \
                     + phelper1(stmt, low, k - 1, True) * phelper1(stmt, k + 1, high, True)
        elif stmt[k] == '|' and not b:
            count += phelper1(stmt, low, k - 1, False) * phelper1(stmt, k + 1, high, False)
        elif stmt[k] == '^' and b:
            count += phelper1(stmt, low, k - 1, True) * phelper1(stmt, k + 1, high, False) \
                     + phelper1(stmt, low, k - 1, False) * phelper1(stmt, k + 1, high, True)
        elif stmt[k] == '^' and not b:
            count += phelper1(stmt, low, k - 1, True) * phelper1(stmt, k + 1, high, True) \
                     + phelper1(stmt, low, k - 1, False) * phelper1(stmt, k + 1, high, False)
    return count

p1("T|T&F^T")
p1("T^F|F")

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

