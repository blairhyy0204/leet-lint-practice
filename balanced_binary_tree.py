"""
[Lintcode 93] Balanced Binary Tree
Link: https://www.lintcode.com/problem/93

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def __init__(self):
        self.balanced = True

    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        if root is None:
            return self.balanced

        self.height(root)
        return self.balanced
        
    def height(self, root: TreeNode):
        if root is None:
            return 0 
        l_height = self.height(root.left)
        r_height = self.height(root.right)

        # the length difference between the l and r paths for a balanced tree can not exceed 1
        if abs(l_height - r_height) > 1:
            self.balanced = False

        # the height of a node depends on the longest path
        return 1 + max(l_height, r_height)