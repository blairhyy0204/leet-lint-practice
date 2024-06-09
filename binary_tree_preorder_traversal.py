"""
[LintCode 66] Binary Tree Preorder Traversal
Link: https://www.lintcode.com/problem/66/description

Given a binary tree, return the preorder traversal of its nodes' values.
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        result = []
        def preorder(root):
            if root is None:
                return

            result.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return result