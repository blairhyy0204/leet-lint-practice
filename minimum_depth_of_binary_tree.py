"""
[LintCode155] Minimum Depth of Binary Tree
Link: https://www.lintcode.com/problem/155

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        # write your code here
        # BFS
        if root is None:
            return 0

        q = [root]
        depth = 0
        while q:
            depth += 1
            new_q = []
            for i in q:
                if not i.left and not i.right:
                    return depth

                if i.left:
                    new_q.append(i.left)
                if i.right:
                    new_q.append(i.right)

            q = new_q
