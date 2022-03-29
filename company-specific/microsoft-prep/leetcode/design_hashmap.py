class MyHashMap:

    def __init__(self):
        self.size = 5000
        self.map = [list()] * self.size
        

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        
        found = False
        if self.map[idx]:
            for i, kv in enumerate(self.map[idx]):
                if kv[0] == key:
                    found = True
                    del self.map[idx][i]
                    self.map[idx].append((key, value))
                    break
        if not found:
            self.map[idx].append((key, value))
                    

    def get(self, key: int) -> int:
        idx = self.hash(key)
        
        if self.map[idx]:
            for k, v in self.map[idx]:
                if k == key:
                    return v   
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        
        for i, kv in enumerate(self.map[idx]):
            if kv[0] == key:
                del self.map[idx][i]
                
    
    def hash(self, key) -> int:
        return key % self.size 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)