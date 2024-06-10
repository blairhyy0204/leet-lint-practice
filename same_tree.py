"""
[LintCode 469]Same Tree
Link: https://www.lintcode.com/problem/469/

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def is_identical(self, a: TreeNode, b: TreeNode) -> bool:
        # write your code here
        # traverse the tree
        if a is None and b is None:
            return True

        if a is None or b is None or a.val != b.val:
            return False
 
        return self.is_identical(a.left, b.left) and self.is_identical(a.right, b.right)