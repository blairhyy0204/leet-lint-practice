"""
[Lintcode 458] Last Position of Target
Link: https://www.lintcode.com/problem/458/

Find the last position of a target number in a sorted array. Return -1 if target does not exist.
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        # right bound
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        if r < 0 or r > len(nums):
            return -1 
    
        return r if nums[r] == target else -1

        