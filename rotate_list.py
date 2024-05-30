"""
[Lint170] Rotate List
Link: https://www.lintcode.com/problem/170

Given a list, rotate the list to the right by k places, where k is non-negative.
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

# Time: O(n)
# Space: O(1)
class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if head is None or k == 0:
            return head
        
        # fast
        f = head
        i = 0
        while i < k:
            if f is None:
                f = head.next
            else:
                f = f.next
            i += 1
        
        # no rotation needed
        if f is None:
            return head

        # slow
        s = head
        while f.next:
            s = s.next
            f = f.next
        
        temp = s.next
        s.next = None
        f.next = head

        return temp