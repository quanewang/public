"""
Given a fraction. Convert it into a decimal.
eg.
10/2 = 5
3/5 = 0.6
If the decimals are repeating recursively, then enclose them inside  ().
eg.
8/3 = 2.(6)

as 8/3 = 2.66666666.......  infinitly.
"""

def fraction(a, b):
    head = str(a/b)
    tail = []
    rem = []
    while a%b != 0 and a%b not in rem:
        rem.append(a%b)
        a = a%b * 10
        tail.append(a/b)
    if a%b == 0:
        return print_fraction(head, tail, False)
    elif a%b in rem:
        return print_fraction(head, tail, True)

def print_fraction(head, tail, recursive):
    if not tail:
        return head
    elif not recursive:
        return head + '.' + ''.join(map(str, tail))
    else:
        return head + '.(' + ''.join(map(str, tail)) + ")"

print fraction(2, 3)
print fraction(8, 3)
print fraction(3, 8)

