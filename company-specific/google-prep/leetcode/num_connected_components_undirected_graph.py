def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
    parents = dict()
    for i in range(n):
        parents[i] = i
        
    for edge in edges:
        x, y = max(edge), min(edge)
        self.union(x, y, parents)
    
    roots = set()
    for i in range(n):
        roots.add(self.find(i, parents))
        
    return len(roots)
        
        
def union(self, x, y, parents):
    parents[self.find(y, parents)] = self.find(x, parents)
    
def find(self, x, parents):
    while parents[x] != x:
        parents[x] = parents[parents[x]] #path compression
        x = parents[x]
    
    return x