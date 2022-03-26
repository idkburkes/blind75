class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.leftnode = Node(None, None)
        self.rightnode = Node(None, None)
        self.leftnode.right = self.rightnode
        self.rightnode.left = self.leftnode
        
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # remove previous node in linked-list
        if key in self.map:
            prev = self.map[key]
            self.remove(prev)
        
        # overwrite value in map and add new node to linkedlist
        new_node = Node(key, value)
        self.add(new_node)
        self.map[key] = new_node
            
        # check if LRU is full
        if len(self.map) > self.capacity:
            # evict the LRU
            lru = self.leftnode.right
            self.remove(lru)
            # remove key from map
            del self.map[lru.key]
            
            
    def remove(self, node):
        # remove from linked-list
        left = node.left
        right = node.right
        left.right = right
        right.left = left
    
        
    def add(self, node):
        # add node to linkedlist
        prev = self.rightnode.left
        prev.right = node
        self.rightnode.left = node
        node.left = prev
        node.right = self.rightnode