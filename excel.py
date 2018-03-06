"""
Given the sequence S1 = {a,b,c,d, ,x,y,z,aa,ab,ac... }
and given that this sequence corresponds (term for term)
to the sequence S2 = {0,1,2,3,...}. Write code to convert
an element of S2 to the corresponding element of S1.
"""



"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""


"""
Given a positive integer, return its corresponding column title as 
appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
def excel(s):
    if s==0:
        return ''
    s-=1
    range=1
    power=0
    while s>=range*26:
        range*=26
        power+=1
        s-=range
    result=''
    while range>0:
        r1= s//range
        result = result + chr(ord('A')+r1)
        s = s % range
        range = range//26
    return result

print excel(0), excel(1),excel(26),excel(27),excel(28),excel(52),excel(51)


print [excel(i) for i in range(1000, 1100)]