from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        # build adjacency list
        graph = probs = dict()
        
        for i in range(len(edges)):
            u, v = edges[i][0], edges[i][1]
            # i like using this setdefault method, try this again in future
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
            probs[(u,v)] = succProb[i]
            probs[(v,u)] = succProb[i]
            
        
        # we convert this to a maxheap by multiplying
        # all the other probabilities by -1
        maxheap = [(-1, start)]
        visited = set()
        
        while maxheap:
            
            prob, node = heappop(maxheap)
            # reached destination
            if node == end: return -prob
            
            # mark this node as visited
            visited.add(node)
            
            for nei in graph.get(node, []):
                # skip if seen
                if nei in visited: continue
                    
                # multiply to get new prob and push back to max heap    
                probUV = probs.get((node,nei)) 
                heappush(maxheap, (prob * probUV, nei))
        
        # return 0 if not found
        return 0
            
            
            
            
            
        
        