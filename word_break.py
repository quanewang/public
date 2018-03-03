"""
-- LESSON
-- breaks[:1] => break[1:]   DEAD LOOP

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        ok=[True]
        for i in range(1, len(s)+1):
            ok.append(False)
            for j in range(i):
                if ok[j] and s[j:i] in wordDict:
                    ok[i] = True
        return ok[len(s)]

s = Solution()
print s.wordBreak("bccdbacdbdacddabbaaaadababadad",
["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"])