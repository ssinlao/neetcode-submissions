# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach
        
        # pointers
        prev, curr = None, head

        while curr:
            tempNext = curr.next # store next node data
            curr.next = prev # set next node addr to prev data
            prev = curr # set prev addr to curr data
            curr = tempNext # change curr to next
        return prev