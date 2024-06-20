"""
[LintCode 1122]Add One Row to Tree
Link: https://www.lintcode.com/problem/1122

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
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
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def add_one_row(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # write your code here
        # BFS
        # Find the layer at depth d and add TreeNode and reconstruct
        n = 1

        if n == d:
            result = TreeNode(val=v)
            result.left = root
            return result

        q = [root]
        while q:
            new_q = []
            for i in q:
                if i.left:
                    new_q.append(i.left)
                if i.right:
                    new_q.append(i.right)

            n += 1
            if n == d:
                break
            q = new_q

        for i in q:
            temp_l = i.left
            temp_r = i.right

            i.left = TreeNode(val=v)
            i.left.left = temp_l
            i.right = TreeNode(val=v)
            i.right.right = temp_r
        return root

