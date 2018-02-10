'''
496187
xxx1xx
pos=2:
496 * pow(10, pos) + (max(0, min(187-200 + 1, 100))
'''

def count_twos(num):
    total = 0
    num_len=len(str(num))
    pos = 0
    while pos<num_len:
        count = num / pow(10, pos+1)
        total += count * pow(10, pos)
        total += max(0, min(num % pow(10, pos+1) - 2 * pow(10, pos)+1, pow(10, pos)))
        pos += 1
    return total

def count_twos_verify(num):
    total = 0
    for n in range(num+1):
        digits = list(str(n))
        for digit in digits:
            if digit=='2':
                total += 1
    return total
print count_twos(28)
print count_twos_verify(28)  
print count_twos(20898)
print count_twos(218)        
print count_twos_verify(20898)
print count_twos_verify(218)





