"""
[LintCode470] Tweaked Identical Binary Tree
Link: https://www.lintcode.com/problem/470/

Check whether two binary trees are equivalent after several twists. Twist is defined as exchanging left and right subtrees of any node. The definition of equivalence is that two binary trees must have the same structure, and the values of nodes in corresponding positions must be equal.
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
    @return: true if they are tweaked identical, or false.
    """
    def is_tweaked_identical(self, a: TreeNode, b: TreeNode) -> bool:
        # write your code here
        # Recursion
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val :
            return False


        return (self.is_tweaked_identical(a.left, b.left) and self.is_tweaked_identical(a.right, b.right)) or (self.is_tweaked_identical(a.right, b.left) and self.is_tweaked_identical(b.right, a.left))