"""
[Lintcode 453] Flatten Binary Tree to Linked List
Link: https://www.lintcode.com/problem/453

Flatten a binary tree to a fake "linked list" in pre-order traversal.
Here we use the right pointer in TreeNode as the next pointer in ListNode
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        if root is None or (root.left is None and root.right is None):
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            sec = root.right
            if sec:
                t = root.left
                while t.right:
                    t = t.right
                t.right = sec
            root.right = root.left
            root.left = None


