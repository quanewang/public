'''
496187
xxx1xx
pos=2: 496 * pow(10, pos)

496287
xxx2xx
496 * 1000 + 88
pos=2: 496 * pow(10, pos) + (num % pow(10, pos) + 1)

496387
xxx3xx
496 * 1000 + 100
pos=2: 496 * pow(10, pos) + pow(10, pos)

'''

def count_twos(num):
    total = 0
    digits = list(str(num))[::-1]
    pos = 0
    for digit in digits:
        count = num / pow(10, pos+1)
        total += count * pow(10, pos)
        if digit=='2':
            total += num % pow(10, pos) + 1
        elif digit>'2':
            total += pow(10, pos)
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

print count_twos(496187)
print count_twos_verify(496187)
print count_twos(496287)
print count_twos_verify(496287)
print count_twos(496587)
print count_twos_verify(496587)