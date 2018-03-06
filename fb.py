"""
1.
1,184->one thousand one hundrd eighty four
- miss result='' check for thousand
- miss and for 208
2.
a)bst check(node, min_val, max_val)
b)[1,3,5]=>[3*5, 1*5, 1*3]
3.
dot multiply [1, 0, 1, 1].[2, 3, 1, 4]
- needed hint
4.
a)1->abc, 2->cde, 12->ac, ad, ae, bc, bd, be...
b)sticks([5, 7, 9], 4)
-needed hint
"""
def mul(a):
    result=[1]*len(a)
    m=1
    for i in range(len(a)):
        result[i]=m
        m*=a[i]
    m=1
    for i in range(len(a)-1, -1, -1):
        result[i]=result[i]*m
        m*=a[i]
    return result
print mul([1, 3, 5])

