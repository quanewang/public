"""
--LESSON
-- minDistance(word1[:i] + word1[i+1:], word2) => 1 + minDistance(word1[:i] + word1[i+1:], word2)

Given two words word1 and word2, find the minimum number of steps
required to make word1 and word2 the same, where in each step you
can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""

def minDistance(word1, word2):
    if not word1 or not word2:
        return len(word1) + len(word2)
    if len(word1)>len(word2):
        word1, word2 = word2, word1
    if is_embedded(word1, word2):
        return len(word2) - len(word1)
    distance = len(word1) + len(word2)
    for i in range(len(word1)):
        distance = min(distance, 1 + minDistance(word1[:i] + word1[i+1:], word2))
    return distance

def is_embedded(word1, word2):
    i = j= 0
    while i<len(word1) and len(word2)-j>=len(word1)-i:
        if word1[i] == word2[j]:
            i += 1
        j += 1
    return i==len(word1)

print minDistance("seat", "eat")