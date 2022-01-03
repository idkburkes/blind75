# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        trail, lead = head, head
        for _ in range(n):
            lead = lead.next
            if not lead:
                return head.next
        while lead and lead.next:
            lead = lead.next
            trail = trail.next
        trail.next = trail.next.next
        return head