"""
Leetcode 19. Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        i = 0
        while fast:
            if i == n:
                break

            fast = fast.next
            i += 1

        if fast is None:
            if i == n:
                return head.next
            else:
                return None 

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head