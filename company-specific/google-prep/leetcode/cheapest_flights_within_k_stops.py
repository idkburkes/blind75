from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        shortest_dist = [float('inf') for _ in range(n)]
        shortest_stops = [float('inf') for _ in range(n)]
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        shortest_dist[src] = 0
        shortest_stops[src] = 0
        
        for u, v, w in flights:
            adj_matrix[u][v] = w
        
        minheap = [(0,0,src)]
        
        while minheap:
            
            dist, stops, cur = heappop(minheap)
            
            # found destination
            if cur == dst:
                return dist
            
            #reached max stops away from source
            if stops == k + 1:
                continue
            
            for nei in range(n):
                # if this neighbor has an edge from current node
                if adj_matrix[cur][nei] > 0:
                    dU = dist
                    dV = shortest_dist[nei]
                    wUV = adj_matrix[cur][nei]
                
                    if dU + wUV < dV:
                        shortest_dist[nei] = dU + wUV
                        heappush(minheap, (dU + wUV, stops + 1, nei))
                        shortest_stops[nei] = stops
                    elif stops < shortest_stops[nei]:
                        heappush(minheap, (dU + wUV, stops + 1, nei))

                    
                
        return -1 if shortest_dist[dst] == float('inf') else shortest_dist[dst]