"""
[Lint165] Merge Two Sorted Lists
Link: https://www.lintcode.com/problem/165

Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
"""

from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(val=0)
        pd = dummy
        p1 = l1
        p2 = l2

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