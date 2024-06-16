"""
[LintCode 1126] Merge Two Binary Trees
Link: https://www.lintcode.com/problem/1126

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
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
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """

    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Write your code here
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        result = TreeNode(val=t1.val + t2.val)

        result.left = self.merge_trees(t1.left, t2.left)
        result.right = self.merge_trees(t1.right, t2.right)
        

        return result