"""
Given a pattern as below and an integer n your task is to decode it and print nth row of it. The pattern follows as :
1
11
21
1211
111221
"""

def conway(n):
    if n==0:
        return ''
    if n==1:
        return '1'
    result = read(conway(n-1))
    return result

def read(text):
    result = ''
    i=0
    while i<len(text):
        c = text[i]
        count=1
        while (i+count)<len(text) and text[i+count]==c:
            count += 1
        result = result + str(count) + text[i]
        i += count
    return result

for i in range(30):
    print conway(i)