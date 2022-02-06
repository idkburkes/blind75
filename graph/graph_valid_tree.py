class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parents = dict()
        for i in range(n):
            parents[i] = i
            
        def find(x, parents):
            node = x
            trail = [node]
            while parents[node] != node:
                node = parents[node]
                trail.append(node)
            for t in trail:
                parents[t] = node
            return node
        
        for edge in edges:
            root1 = find(edge[0], parents)
            root2 = find(edge[1], parents)
            if root1 == root2:
                return False
            parents[root1] = parents[root2]
                
        return True
            
           
