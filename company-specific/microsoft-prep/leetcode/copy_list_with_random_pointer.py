"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        prev = None
        copies = dict()
        # first pass to find all nodes in linked-list
        while cur:
            copies[cur] = Node(cur.val)
            
            if cur.next:
                copies[cur.next] = Node(cur.next.val)
                copies[cur].next = copies[cur.next]
            
            if prev:
                copies[prev].next = copies[cur]  

            prev = cur.next
            if cur.next:
                cur = cur.next.next
            else:
                cur = cur.next #end of linked-list
        
            
        # second pass to fill random pointers
        cur = head
        while cur:
            if cur.random:
                copies[cur].random = copies[cur.random]
            cur = cur.next
        
        
        return copies[head]