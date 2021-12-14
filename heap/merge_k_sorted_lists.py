from heapq import *
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head_ptrs, min_heap = [], []

        if len(lists) == 1:
            return lists[0]
        
        head_ptrs = [None] * len(lists)

        for i in range(len(lists)):
            if lists[i]:
              head = (lists[i].val, i) # (currentheadval, index of head)
              head_ptrs[i] = lists[i]
              heappush(min_heap, head)
        res = None
        cur = None
        while min_heap:
            val, head_index = heappop(min_heap)
            if res:
                new_node = ListNode(val)
                cur.next = new_node
                cur = cur.next  
            else:
                res = ListNode(val)
                cur = res
            if head_ptrs[head_index].next:
                head_ptrs[head_index] = head_ptrs[head_index].next
                next_val = head_ptrs[head_index].val
                heappush(min_heap, (next_val, head_index))
        return res



        
        

        



        