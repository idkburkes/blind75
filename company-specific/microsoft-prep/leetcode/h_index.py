class Solution:
    # sorting the array for this solution gives nlogn time complexity
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations = sorted(citations)
        
        h = 0
        for i in range(n):
            if citations[i] >= n - i:
                h = max(n - i, h)
        
        return h

    # this is the optimal counting sort solution with O(n) time
    def hIndexOptimal(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0 for _ in range(n+1)]
        
        for citation in citations:
            counts[min(citation, n)] += 1
            
        res = 0
        for i in range(n, -1, -1):
            if i != n:
                counts[i] += counts[i+1]
            if counts[i] >= i:
                res = max(res, i)
        
        return res
        
        
        
            
            
        
        
        
            
            
        
        
        