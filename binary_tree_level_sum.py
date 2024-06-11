"""
[LintCode 482] Binary Tree Level Sum
Link: https://www.lintcode.com/problem/482/

Given a binary tree and an integer which is the depth of the target level.
Calculate the sum of the nodes in the target level.
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
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        # BFS
        if root is None:
            return 0

        q = [root]

        n = 1

        while q:
            if n - level == 0:
                result = 0
                for i in q:
                    result += i.val
                return result

            new_q = []
            for i in q:
                if i.left:
                    new_q.append(i.left)
                if i.right:
                    new_q.append(i.right)
            q = new_q
            n +=1 

        # level is larger than depth
        return 0