class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <=1:
            return n
        parents = dict()
        for i in range(n):
            parents[i] = i
        
        for edge in edges:
            high, low = max(edge[0],edge[1]), min(edge[0],edge[1])
            self.union(high, low, parents)
        
        roots = set()
        for i in range(n):
            roots.add(self.find(i, parents))
        return len(roots)
        
    
    def union(self, x, y, parents):
        parents[self.find(y, parents)] = self.find(x, parents)
    
    def find(self, x, parents):
        node = x   
        #Trail of nodes that undergo path compression
        trail = [node]
        while parents[node] != node:
            node = parents[node]
            trail.append(node)
        # Path compression greatly increases speed of union find!
        for c in trail:
            parents[c] = node
        return node