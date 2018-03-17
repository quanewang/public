"""
https://leetcode.com/problems/all-oone-data-structure/description/
432. All O`one Data Structure
DescriptionHintsSubmissionsDiscussSolution
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""

class KeyList:
    def __init__(self):
    def incKey(self, node):
        if not self.head:
            self.head=self.tail=node
        else:
            self.tail.right=node
            node.left = self.tail
            node.right = None
            self.tail = node

class KeyNode:
    def __init__(self):
        self.left=None
        self.right=None
        self.value=None

class Keys:
    def __init__(self):
        self.h={}
        self.head=None
        self.tail=None
    def addKey(self, key):
        if key in self.h:
            raise Exception()
        node = self.insert(key)
        self.h[key]=node

    def rmKey(self, key):
        if key not in self.h:
            raise Exception()
        self.remove(key)
        self.h.pop(key)

    def insert(self, key):
        pass
    def remove(self, key):
        pass


class AllOneNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.keys = Keys()


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        self.head = None
        self.tail = None

    def add(self, key):
        if self.head==None:
            node = AllOneNode()
            node.value=1
            node.keys.addKey(key)
            self.head = node
            self.tail = node
        else:
            if self.tail.value==1:
                self.tail.keys.addKey(key)
            else:
                node=AllOneNode()
                node.value=1
                node.keys.addKey(key)
                self.tail.right=node
                node.left = self.tail
                self.tail = node

    def move_left(self, node, key):
        if not node.left:
            new_node = AllOneNode()
            new_node.value=node.value+1
            new_node.right=node
            node.left=new_node
            self.head=new_node
        else:
            new_node = node.left
        new_node.keys.addKey(key)
        node.keys.removeKey(key)
        if not node.keys:
            new_node.right = node.right
            if not node.right:
                self.tail = new_node
            else:
                node.right.left = new_node
        return new_node

    def move_right(self, node, key):
        if not node.right:
            if node.value>1:
                new_node = AllOneNode()
                new_node.value = node.value - 1
                new_node.left = node
                node.right = new_node
                self.tail=new_node
            else:
                new_node=None
            node.keys.remove(key)
        elif node.right.value==node.value-1:
            new_node = node.left
        new_node.keys.addKey(key)
        node.keys.removeKey(key)
        if not node.keys:
            new_node.right = node.right
            if not node.right:
                self.tail = new_node
            else:
                node.right.left = new_node
        return new_node


    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.h:
            node = self.h[key]
            new_node=self.move_left(node, key)
            self.h[key]=new_node
        else:
            node = self.add(key)
            node[key]=node


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.h:
            raise Exception()
        else:
            node = self.h[key]
            new_node = self.move_right(node)
            if not new_node:
                self.h.pop(key)
            else:
                self.h[key]=new_node

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head:
            return self.head.keys.head.value
        return None

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.tail:
            return self.tail.keys.head.value
        return None



        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()