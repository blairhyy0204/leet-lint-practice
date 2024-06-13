"""
[Lintcode 177] Convert Sorted Array to Binary Search Tree With Minimal Height
Link: https://www.lintcode.com/problem/177/

Given a sorted (increasing order) array, Convert it to a binary search tree with minimal height.
"""

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: an integer array
    @return: A tree node
    """
    def sorted_array_to_b_s_t(self, a: List[int]) -> TreeNode:
        # write your code here
        if len(a) == 0:
            return None

        if len(a) == 1:
            return TreeNode(val=a[0])

        mid = (len(a)-1) // 2
        res = TreeNode(val=a[mid])
        res.left = self.sorted_array_to_b_s_t(a[:mid])
        res.right = self.sorted_array_to_b_s_t(a[mid+1:])

        return res

