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

def convert(n):
    result = ''
    units=['', 'thousand', 'million', 'billion']
    a = partition(n)
    for i in range(len(a)-1, -1, -1):
        p = print_xxx(a[i], i==0)
        result += p + ' '
        if p!='':
            result += units[i] + ' '
    return result

def print_xxx(n, is_last):
    result=''
    ones=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    teens=["ten", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
    if n>99:
        result += ones[n//100] + ' hundred '
    if n%100>=20:
        result += tens[n%100//10] + ' '
    elif n%100>=10:
        result += teens[n%10] + ' '
        return result
    elif n==0:
        if is_last:
            return 'zero'
    if n%10>0:
        result+=ones[n%10]
    return result

def partition(n):
    t=str(n)
    r=[]
    while n>1000:
        r.append(n%1000)
        n = n//1000
    r.append(n)
    return r

print convert(12321132)