from heapq import heappush, heappop
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        
        # Dijkstra's using an adjacency list
        graph = collections.defaultdict(list)
        visited =dict()
        costs = dict()
        
        for edge in highways:
            u, v, w = edge
            graph[u].append(v)
            graph[v].append(u)
            costs[(u,v)] = w
            costs[(v,u)] = w
        
        # start at source
        minheap = [(0, 0, discounts)]
        
        while minheap:
            
            cost, node, discount = heappop(minheap)
            if node == n - 1:
                # reached destination 
                return cost
            
            if node in visited and discount <= visited[node]:
                continue
            
            visited[node] = discount
            
            for nei in graph[node]:
                # I don't quite understand this part yet.
                # Why are we allowed to add 2 edges to the path and still come out with the optimal answer?
                if discount > 0:
                    heappush(minheap, (cost + costs[(node, nei)] // 2, nei, discount - 1 ))
                heappush(minheap, (cost + costs[(node, nei)], nei, discount))
        return -1
            
            
            
        
            
        
        