"""
[LintCode 1137] Construct String from Binary Tree
Link: https://www.lintcode.com/problem/1137/

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
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
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t: TreeNode) -> str:
        # write your code here
        # preorder
        if t is None:
            return ""
        
        s= str(t.val) 
        if not t.left and not t.right:
            return s

        s += "("  + self.tree2str(t.left) + ")"
        if t.right:
            s  +=  "("  + self.tree2str(t.right) + ")"
        return s

