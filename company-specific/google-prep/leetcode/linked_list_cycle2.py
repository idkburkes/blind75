# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        fast = slow = head
        
        # Find intersection point
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # Determine if there was no cycle
        if fast is None or fast.next is None:
            return None
        
        # This second part is the power of Floyd's Cycle Detection algorithm
        # The distance from head to start of cycle is the same distance as
        #   from the intersection to the start of the cycle
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return fast