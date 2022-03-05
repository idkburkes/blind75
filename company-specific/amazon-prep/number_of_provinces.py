class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        res = 0
        n = len(isConnected)
        for i in range(n):
            if i not in seen:
                queue = [i]
                while queue:
                    cur = queue.pop(0)
                    seen.add(cur)
                    queue = [k for k,j in enumerate(isConnected[cur]) if j and k not in seen] + queue
                res += 1
        return res
                    
                    
        