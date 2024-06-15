"""
[Lintcode 1524] Search in a Binary Search Tree
Link:
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
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        # Write your code here.
        if root is None: 
            return None

        if root.val == val:
            return root

        left = self.search_b_s_t(root.left, val)
        right = self.search_b_s_t(root.right, val)

        if left:
            return left
        if right:
            return right

        return None

