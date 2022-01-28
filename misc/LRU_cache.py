class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #left is LRU, right is most recent
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    
    def insert(self, node):
        most_recent = self.right.prev
        most_recent.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = most_recent
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        self.insert(node)
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node
           
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)