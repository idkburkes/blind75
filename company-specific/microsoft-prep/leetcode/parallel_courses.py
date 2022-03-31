class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        indegree = [0 for _ in range(n+1)]
        outdegree = dict()
        
        for edge in relations:
            prev, next = edge[0], edge[1]
            indegree[next] += 1
            outdegree.setdefault(prev, []).append(next)
            
        courses_completed = 0
        total_sems = 0
        queue = []
        for i in range(1,n+1):
            if indegree[i] == 0:
                queue.append(i)
                courses_completed += 1
        
        semester_size = len(queue)
        
        while queue:
            for _ in range(semester_size):
                cur = queue.pop(0)
                neighbors = outdegree.get(cur, [])
                for nei in neighbors:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                        courses_completed += 1
            total_sems += 1
            semester_size = len(queue)
        
        return total_sems if courses_completed == n else -1
            
                
        