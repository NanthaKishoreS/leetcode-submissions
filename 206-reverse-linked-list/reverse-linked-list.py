# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        # 1. Reverse the list pointers
        while current:
            nxt = current.next # Best practice: use 'nxt' to avoid built-in name clashes
            current.next = prev
            prev = current 
            current = nxt
            
        # 2. Return the new head node (prev is standing on the new front)
        return prev
