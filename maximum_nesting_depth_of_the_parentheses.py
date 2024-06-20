"""
[LeetCode 1614] Maximum Nesting Depth of the Parentheses
Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        # stack
        depth = 0
        max_dep = 0
        for i in s:
            if i == "(":
                depth += 1
            
            if i == ")":
                max_dep = max(depth, max_dep)
                depth -= 1

        return max_dep