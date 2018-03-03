def reverse(s):
    if not s:
        return s
    x = s.pop()
    reverse(s)
    insert(s, x)
    return s

def insert(s, x):
    if not s:
        s.append(x)
    else:
        y = s.pop()
        insert(s, x)
        s.append(y)


print reverse([1, 2, 3, 4])
