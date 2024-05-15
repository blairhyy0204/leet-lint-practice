"""
[LintCode930] Connected Components in List
Link: https://www.lintcode.com/problem/930/

[LeetCode817] Linked List Components
Link: https://leetcode.com/problems/linked-list-components/

You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.
Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

Example 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_blocks = 0
        start = False
        while head and len(nums) != 0:
            val = head.val
            head = head.next
            if val in nums:
                if not start:
                    num_blocks += 1
                    start = True
            else:
                start = False

        return num_blocks
