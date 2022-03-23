from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict()
        seentimes = dict()
        
        for time in times:
            u, v, w = time[0], time[1], time[2]
            graph.setdefault(u, []).append((v, w))
                  
        heap = [(0, k)]
        
        while heap:    
            time, node = heappop(heap)
            
            if node not in seentimes:
                seentimes[node] = time
                for nei, weight in graph.get(node, []):
                        heappush(heap ,(time + weight, nei))
        
        return max(seentimes.values()) if len(seentimes) == n else -1
                
            
            
            
            
            
        
            
        
            
        