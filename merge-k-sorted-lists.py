"""
Leetcode 23. Merge k Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        dummy = ListNode(-1)
        pd, pl, pr = dummy, left, right

        while pl and pr:
            if pl.val < pr.val:
                pd.next = pl
                pl = pl.next
            else:
                pd.next = pr
                pr = pr.next

            pd = pd.next

        if pl:
            pd.next = pl
        if pr:
            pd.next = pr

        return dummy.next


    def mergeSort(self, lists, low, high):
        if low > high:
            return None

        if low == high:
            return lists[low]  

        mid = (low + high) // 2
        left = self.mergeSort(lists, low, mid)
        right = self.mergeSort(lists, mid+1, high)

        if left and right:
            return self.merge(left, right)

        return left if left else right
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        return self.mergeSort(lists, 0, len(lists)-1)