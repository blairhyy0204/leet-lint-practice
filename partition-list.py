"""
Leetcode 86. Partition List
Link: https://leetcode.com/problems/partition-list

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummySmall = ListNode(-1)
        dummyLarge = ListNode(-1)
        pS, pL, p = dummySmall, dummyLarge, head

        while p:
            if p.val < x:
                pS.next = p
                pS = pS.next
            else:
                pL.next = p
                pL = pL.next
            p = p.next

        # it is crucial to terminate the dummyLarge list, otherwise it will cause a loop in the list
        pL.next = None
        pS.next = dummyLarge.next

        return dummySmall.next