from heapq import heappop, heappush

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        minheap = []
        head_ptrs = [None] * n
        
        # store the first value of each list inside of minheap
        for i in range(n):
            node = lists[i]
            if node:
                # store the value with its index in the original list
                # this is how we keep track of which list the current min-val came from
                pair = (node.val, i)
                heappush(minheap, pair)
                
        # find the min node (will be the head of what we return)
        result_head = None
        if minheap:
            val, i = heappop(minheap)
            node = lists[i]
            result_head = node
            # move this list to the next node
            if node.next:
                heappush(minheap, (node.next.val, i))
                lists[i] = node.next
        
        cur = result_head
        
        while minheap:
            val, i = heappop(minheap)
            node = lists[i]
            
            # add this node to the result linked-list
            cur.next = node
            cur = node
            
            # move this list to the next node and add next node to minheap
            if node.next:
                heappush(minheap, (node.next.val, i))
                lists[i] = node.next
        
        return result_head
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        