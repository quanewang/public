"""
--LESSON
--
            i += 1
            if i<len(text):
              remove(h, text[i])
==>          if i<len(text):
              remove(h, text[i])
            i += 1
-- j<len(char)-1 => j<len(text)-1

Smallest Substring of All Characters
Given an array of unique characters arr and a string str,
Implement a function getShortestUniqueSubstring that finds
the smallest substring of str containing all the characters
in arr. Return "" (empty string) if such a substring doesnt exist.

Come up with an asymptotically optimal solution and analyze
the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
"""

def sub(arr, text):
    if not text or not arr:
        return ''
    i, j = 0, 0
    h = {}
    sub=None
    add(h, text[0], arr)
    while i<len(text):
        if len(h)==len(arr):
            sub = min_sub(sub, text[i:j+1])
            if i<len(text):
              remove(h, text[i])
            i += 1
        elif j<len(text)-1:
            j+=1
            add(h, text[j], arr)
        else:
            break
    return '' if not sub else sub

def add(h, c, arr):
    if c in arr:
        if c in h:
            h[c]=h[c]+1
        else:
            h[c]=1
def remove(h, c):
    if c in h:
        h[c] = h[c] - 1
        if not h[c]:
            h.pop(c)

def min_sub(s1, s2):
    if s1 and len(s1)<=len(s2):
        return s1
    return s2

print sub( ["A","B","C"], "ADOBECODEBANCDDD")