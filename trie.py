class Node:
    def __init__(self):
        self.children={}
        self.value = None

class Trie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not self.root:
            self.root = Node()
        self.insert_helper(self.root, word, 0)

    def insert_helper(self, node, word, idx):
        if not word:
            return
        if idx>=len(word):
            return
        if word[idx] not in node.children:
            child = Node()
            node.children[word[idx]] = child
            if idx==len(word)-1:
                child.value = word
            else:
                child.value = word[idx]
        self.insert_helper(node.children[word[idx]], word, idx+1)

    def traverse(self):
        self.traverse_helper(self.root)

    def traverse_helper(self, node):
        if not node:
            return
        if not node.children:
            print node.value
        for _, child in node.children.items():
            self.traverse_helper(child)

    def list(self, prefix):
        prefix_node = self.search(prefix)
        self.traverse_helper(prefix_node)

    def search(self, prefix):
        return self.search_helper(self.root, prefix)

    def search_helper(self, node, prefix):
        if not prefix:
            return node
        return self.search_helper(node.children[prefix[0]], prefix[1:]) if prefix[0] in node.children else None


t = Trie()
t.insert("abc")
t.insert("abe")
t.insert("cde")
t.traverse()
t.list("a")