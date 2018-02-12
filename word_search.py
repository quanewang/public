"""
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"]
"""

class Solution(object):
    def __init__(self):
        pass

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        for word in words:
            for i in range(0, len(board)):
                for j in range(0, len(board)):
                    if word and word[0] == board[i][j]:
                        h = {}
                        if self.findWord(board, i,j, word, 0, h):
                             result.append(word)
        return result
    def findWord(self, board, x, y, word, i, h):
        if not self.inscope(board, x, y):
            return False
        if self.visited(x, y, h):
            return False
        if i>=len(word):
            return True
        if word[i]==board[x][y]:
            if i==len(word)-1:
                return True
            else:
                self.visit(x, y, h)
                if self.findWord(board, x-1, y, word, i+1, h):
                    return True
                if self.findWord(board, x + 1, y, word, i + 1, h):
                    return True
                if self.findWord(board, x, y+1, word, i + 1, h):
                    return True
                if self.findWord(board, x, y-1, word, i + 1, h):
                    return True
        else:
            return False

    def inscope(self, board, x, y):
        return x<len(board) and y<len(board[0])

    def visit(self, x, y, h):
        h[str(x)+'_'+ str(y)]=1

    def visited(self, x, y, h):
        return (str(x)+'_'+ str(y)) in h

board = [["a","a"]]
words=["aaa"]
words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
s= Solution()
h={}
s.visit(1, 2, h)
print s.visited(1, 2, h)
print s.findWords(board, words)