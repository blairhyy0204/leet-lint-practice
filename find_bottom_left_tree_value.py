"""
[Leetcode 513] Find Bottom Left Tree Value
Link: https://leetcode.com/problems/find-bottom-left-tree-value/description/

Given the root of a binary tree, return the leftmost value in the last row of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None
        self.max_depth = 0

    def dfs(self, root, depth):
        if root is None:
            return 

        if root.left is None and root.right is None:
            if depth > self.max_depth:
                self.res = root.val
                self.max_depth = depth

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
            
        self.dfs(root, 1)
        return self.res