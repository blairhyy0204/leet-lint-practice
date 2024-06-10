"""
[Lint480] Binary Tree Paths
Link: https://www.lintcode.com/problem/480

Given a binary tree, return all root-to-leaf paths.
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        # DFS with post order
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        left_paths = self.binary_tree_paths(root.left)
        right_paths = self.binary_tree_paths(root.right)

        result = []
        for path in left_paths + right_paths:
            path = str(root.val) + "->" + path
            result.append(path)

        return result
