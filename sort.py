def quick(a, l, r):
    n = len(a)
    if l not in range(n) or r not in range(n) or l>=r:
        return
    l0, r0=l, r
    p = a[l]
    while l<r:
        if a[l]>a[r]:
            tmp1, tmp2 = a[r], a[l]
            a[l], a[r] = tmp1, tmp2
        if a[l]==p:
            r -= 1
        else:
            l += 1
    quick(a, l0, l-1)
    quick(a, l+1, r0)

a=[70, 30, 20, 10, 10, 10, 10]
b=[-1, -3, -3, -3, 2, 2, 3, 3]
c=[-1]
d=[-3, -1]

quick(a, 0, len(a)-1)
quick(b, 0, len(b)-1)
quick(c, 0, len(c)-1)
quick(d, 0, len(d)-1)
print a, b, c, d


def merge(a):
    if not a or len(a)==1:
        return a
    result = []
    mid = len(a)//2
    x = merge(a[:mid])
    y = merge(a[mid:])
    i,j = 0,0
    while i<len(x) and j<len(y):
        if x[i]<y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    while i<len(x):
        result.append(x[i])
        i+=1
    while j<len(y):
        result.append(y[j])
        j+=1
    return result


print merge([70, 30, 20, 10, 10, 10, 10])
print merge([70, 30])
