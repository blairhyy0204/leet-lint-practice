"""
[Lint228] Middle of Linked List
Link: https://www.lintcode.com/problem/228/

Find the middle node of a linked list and return it.
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
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        # Method 1: loop through
        # Time: O(n)
        # Space: O(1)

        # find the length
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        half = (n+1) // 2

        while head:
            half -= 1
            if half == 0:
                return head
            head = head.next
        
        return None

        # Method2: Fast and slow pointers
        if not head:
            return None

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow