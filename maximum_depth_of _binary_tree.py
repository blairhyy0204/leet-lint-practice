"""
[LintCode 97] Maximum Depth of Binary Tree
Link: https://www.lintcode.com/problem/97

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        # DFS
        if root is None:
            return 0 

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        return max(left, right) + 1



