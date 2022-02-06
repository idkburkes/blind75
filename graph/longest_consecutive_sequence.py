
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Initialize nodes - Set the parent of each node to itself
        parents = dict()
        for num in nums:
            parents[num] = num
        
        # Connect each node to neighbors both ways if they exist
        for num in nums:
            if num + 1 in parents:
                self.union(num+1, num, parents)
            if num - 1 in parents:
                self.union(num, num-1, parents)
        
        # Find max distance from a node to its parent
        res = 0
        for num in nums:
            dif = self.find(num, parents) - num + 1 
            res = max(res, dif)
        return res
        
    # Search up graph to find parent
    def find(self, x, parents):
        node = x
        while(parents[node] != node):
            node = parents[node]
        return node
    
    # Combine components, set parent of second to the parent of the first 
    def union(self, x, y, parents):
        parents[self.find(y, parents)] = self.find(x, parents)
        
        
        