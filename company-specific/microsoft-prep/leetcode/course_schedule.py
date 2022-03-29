class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completed = 0
        indegree = [0 for _ in range(numCourses)]
        outdegree = dict()
        
        for edge in prerequisites:
            course, prereq = edge[0], edge[1]
            indegree[course] += 1
            outdegree.setdefault(prereq, []).append(course)
        
        queue = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                completed += 1
        
        while queue:
            course = queue.pop(0)
            for next_course in outdegree.get(course, []):
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    completed += 1
        
        return completed == numCourses
        
        
                
            
        
        
        