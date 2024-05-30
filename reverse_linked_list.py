"""
[Lint35] Reverse Linked List
Link: https://www.lintcode.com/problem/35

Reverse a linked list.
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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        cur = None

        while head:
            temp = head.next
            head.next = cur
            cur = head
            head = temp

        return cur