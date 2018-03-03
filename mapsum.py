"""
-- LESSON
-- v.sum(prefix[0]) => v.sum('')

https://leetcode.com/problems/map-sum-pairs/description/
"""

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children={}
        self.value = 0

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if not key:
            self.value = val
        else:
            if key[0] not in self.children:
                self.children[key[0]] = MapSum()
            self.children[key[0]].insert(key[1:], val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if not prefix:
            result = self.value
            for k,v in self.children.iteritems():
                result += v.sum('')
            return result
        elif prefix[0] in self.children:
            return self.children[prefix[0]].sum(prefix[1:])
        return 0



        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)