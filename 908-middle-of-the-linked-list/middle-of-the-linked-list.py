# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        tortise = head

        while rabbit and rabbit.next:
            tortise = tortise.next
            rabbit = rabbit.next.next

        return tortise
