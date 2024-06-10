"""
[LintCode 481] Binary Tree Leaf Sum
Link: https://www.lintcode.com/problem/481

Given a binary tree, calculate the sum of leaves.
"""

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
    @param root: the root of the binary tree
    @return: An integer
    """
    def leaf_sum(self, root: TreeNode) -> int:
        # write your code here
        # divide and conquer. get to the leaves
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val
        
        return self.leaf_sum(root.left) + self.leaf_sum(root.right)
        

