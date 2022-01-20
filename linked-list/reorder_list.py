# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from calendar import c


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse from midpoint        
        cur = slow.next
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        slow.next = None
        
        # Merge lists
        left_head, right_head = head, prev
        while right_head:
            left_next = left_head.next
            left_head.next = right_head
            left_head = right_head
            right_head = left_next


            


