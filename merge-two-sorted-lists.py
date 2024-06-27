"""
Leetcode 21. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0)
        pd = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                pd.next = p1
                p1 = p1.next
            else:
                pd.next = p2
                p2 = p2.next
            pd = pd.next

        if p1:
            pd.next = p1
        
        if p2:
            pd.next = p2
        
        return dummy.next

