"""
[Leetcode 298] Binary Tree Longest Consecutive Sequence
Link: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/

Given the root of a binary tree, return the length of the longest consecutive sequence path.
A consecutive sequence path is a path where the values increase by one along the path.
Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = float('-inf')
    
    def traverse(self, node, length):
        if length > self.max_length:
            self.max_length = length

        if node.left:
            if node.left.val == node.val + 1:
                self.traverse(node.left, length+1)
            else:
                self.traverse(node.left, 1)
        
        if node.right:
            if node.right.val == node.val + 1:
                self.traverse(node.right, length+1)
            else:
                self.traverse(node.right, 1)
        
        
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 1)
        return self.max_length