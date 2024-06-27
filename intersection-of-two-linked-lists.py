"""
Leetcode 160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB

        while pa or pb:
            if not pa:
                pa = headB
            if not pb:
                pb = headA

            if pa == pb:
                return pa

            pa = pa.next
            pb = pb.next

        return None