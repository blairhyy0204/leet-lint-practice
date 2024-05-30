"""
[Lint452] Remove Linked List Elements
Link: https://www.lintcode.com/problem/452

Remove all elements from a linked list of integers that have value val.
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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        # Method 1: create a new linked list
        # Time: O(n)
        # Space: O(n)
        dummy = ListNode(val = 0)
        pd = dummy
        p = head

        while p is not None:
            if p.val != val:
                pd.next = ListNode(val=p.val)
                pd = pd.next

            p=p.next
        return dummy.next

        # Method 2: modify the linked list directly
        # Time: O(n)
        # Space: O(1)
        # When needing to check the 1st ListNode of a linked list, use dummy head
        dummy = ListNode(val=0, next=head)
        p = dummy

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                # move to next if next doesn't have val
                p = p.next
        
        return dummy.next