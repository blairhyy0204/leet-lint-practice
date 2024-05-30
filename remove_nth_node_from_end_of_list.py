"""
[Lint174] Remove Nth Node From End of List
Link: https://www.lintcode.com/problem/174

Given a linked list, remove the nth node from the end of list and return its head.
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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        dummy = ListNode(val=0, next=head)
        # fast pointer
        f = dummy
        for i in range(n):
            f = f.next

        # slow
        s = dummy
        while f.next:
            f = f.next
            s = s.next
        
        s.next = s.next.next

        return dummy.next