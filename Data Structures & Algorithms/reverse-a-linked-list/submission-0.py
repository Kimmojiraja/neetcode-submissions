# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:

            nextt = current.next # because we are securing for the next element
            current.next = prev # reversing the nodes

            # now two pointers
            prev = current
            current = nextt # moving one step ahead 
        return prev





        