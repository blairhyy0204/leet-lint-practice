"""
[Lint219] Insert Node in Sorted Linked List
Link: https://www.lintcode.com/problem/219/

Insert a node in a sorted linked list.
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

# time: O(n)
# space: O(1)
class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insert_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        if head is None:
            return ListNode(val, next=None)
        
        if head.val >= val:
            return ListNode(val, next = head)

        cur = head
        while cur:
            if not cur.next or cur.next.val >= val:
                second = cur.next
                node = ListNode(val, next=second)
                cur.next = node
                break
            
            cur = cur.next

        return head
