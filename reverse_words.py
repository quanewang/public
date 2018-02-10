

def reverse_words(words):
    reverse(words, 0, len(words)-1)
    prev = 0
    for i in range(0, len(words)):
        if not words[i].strip():
            reverse(words, prev, i-1)
            prev = i + 1
    if prev<len(words):
        reverse(words, prev, len(words)-1)
    return words


def reverse(words, begin, end):
    while(begin<end):
        tmp = words[begin]
        words[begin] = words[end]
        words[end] = tmp
        begin += 1
        end -= 1

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print reverse_words(arr)