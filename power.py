def power(x, n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n<0:
        return float(1)/power(x, (-1)*x)
    m=[1]*(n+1)
    m[1]=x
    for i in range(2, n+1):
        mid = i//2
        m[i]=m[mid]*m[i-mid]
    return m[n]

print power(2, 2)