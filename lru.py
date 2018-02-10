'''
LESSON
-         if page in self.usage:
           self.usage.remove(page)
- dict.pop(key)
- list.remove(value)
- list[:5]
- list[1:]
'''
# Question 8: Implement LRU Cache

class LRU:
    capacity = 2
    index = {}
    usage = []
    def put(self, page, data):
        if page not in self.index and len(self.index)>=self.capacity:
            self.index.pop(self.usage[0])
            self.usage = self.usage[1:]
            print self.index, self.usage
        self.index[page] = data
        if page in self.usage:
           self.usage.remove(page)
        self.usage.append(page)
        print self.index, self.usage

    def get(self, page):
        result = None
        if page in self.index:
            result = self.index[page]
            self.usage.remove(page)
            self.usage.append(page)
            print page, self.usage
        return result

lru = LRU()
print lru.get(1)
lru.put(1, 1)
print lru.get(1)
lru.put(2, 2)
print lru.get(1)
lru.put(3, 3)
print lru.get(3)
print lru.get(1)