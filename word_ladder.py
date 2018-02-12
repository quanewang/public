"""
LESSON
-- mising "return result"
-- return word; => return result;
-- self.find(self,...
-- shortest
-- if not result => if result

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        result = []
        if endWord not in wordList:
            return result
        progres=[beginWord]
        self.find(beginWord, endWord, wordList, progres, result)
        return result

    def find(self, beginWord, endWord, wordList, progress, result):
        if self.close(beginWord, endWord):
            self.add(result, progress, endWord)
            return
        if result:
            if len(result[0])<=len(progress):
                return
        close_words = self.find_unused_close_words(beginWord, wordList, progress)
        for word in close_words:
            progress.append(word)
            self.find(word, endWord, wordList, progress, result)
            progress.pop()

    def close(self, word1, word2):
        if word1==None or word2==None:
            return False
        if len(word1) != len(word2):
            return False
        count = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                count +=1
        return count<2

    def find_unused_close_words(self,beginWord, wordList, progress):
        result = []
        for word in wordList:
            if self.close(beginWord, word) and word not in progress:
                result.append(word)
        return result;

    def add(self, result, progress, endWord):
        result_progress = list(progress)
        if endWord not in progress:
            result_progress.append(endWord)
        shortest = len(result_progress)
        result.append(result_progress)
        removed=[]
        for entry in result:
            if len(entry)>shortest:
                removed.append(entry)
        for entry in removed:
            result.remove(entry)



s= Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print s.findLadders(beginWord, endWord, wordList)
