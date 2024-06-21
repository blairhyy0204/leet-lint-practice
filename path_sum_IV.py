"""
[Leetcode 666] Path Sum IV
Link: https://leetcode.com/problems/path-sum-iv

If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

The hundreds digit represents the depth d of this node where 1 <= d <= 4.
The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
The units digit represents the value v of this node where 0 <= v <= 9.
Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.
"""

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        memo = [[[0, 0] for _ in range(8)] for _ in range(4)]
        for i in nums[::-1]:
            level = i // 100 - 1
            idx = ( i // 10 ) % 10 - 1
            dig = i % 10 

            memo[level][idx][1] = dig
            if memo[level][idx][0] == 0:
                memo[level][idx][0] = 1

            parent_idx = idx // 2
            if level - 1 >= 0: 
                memo[level-1][parent_idx][0] += memo[level][idx][0]

        result = 0
        for m in memo:
            for q in m:
                result += q[0] * q[1]
            
        return result