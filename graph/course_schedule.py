
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        finished = 0
        queue = []
        indegree = [[] for course in range(numCourses)]
        outdegree = [0 for course in range(numCourses)]
        for prereq in prerequisites:
            outdegree[prereq[0]] += 1
            indegree[prereq[1]].append[prereq[0]]
        for i in range(numCourses):
            if outdegree[i] == 0:
                queue.append(i)
                finished += 1
        
        while queue:
            cur = queue.pop(0)
            for num in indegree[cur]:
                outdegree[num] -= 1
                if outdegree[num] == 0:
                    queue.append(num)
                    finished += 1
        return finished == numCourses
        
            
            
