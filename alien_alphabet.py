"""
Given a sorted dictionary of an alien language having N words
and k starting alphabets of standard dictionary the task is
to complete the function which returns a string denoting
the order of characters in the language..

Note: Many orders may be possible for a particular test case, thus you may return any valid order.


Examples:

Input:  Dict[] = { "baa", "abcd", "abca", "cab", "cad" }, k = 4
Output: Function returns "bdac"
"""

def alphabet(words, k):
    chars = []
    all = {}
    if not words:
        return chars
    prev = None
    for i in range(1, len(words)):
        word = words[i]
        if not word:
            continue
        for c in word:
            all[c] = 1
        if prev == None:
            prev = word
            continue
        for j in range(min(len(prev), len(word))):
            if prev[j] != word[j]:
                enter(chars, prev[j], word[j])
            j += 1

    if k>len(chars):
        for key, value in enumerate(all):
            if k>len(chars):
                if key not in chars:
                    chars.append(key)
    return chars

def enter(chars, a, b):
    found_a = False
    found_b = False
    idx_a = None
    idx_b = None
    for i in range(len(chars)):
        if chars[i] == a:
            found_a = True
            idx_a = i
        elif chars[i] == b:
            found_b = True
            idx_b = i
    if found_a and not found_b:
        chars.insert(idx_a+1, b)
    elif not found_a and found_b:
        chars.insert(idx_b, a)
    elif not found_a and not found_b:
        chars.append(a)
        chars.append(b)

print alphabet(["baa", "abcd", "abca", "cab", "cad" ], 4)