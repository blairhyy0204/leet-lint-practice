"""
[LintCode 459]Closest Number in Sorted Array
Link: https://www.lintcode.com/problem/459

Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.
Return -1 if there is no element in the array.
"""
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closest_number(self, a: List[int], target: int) -> int:
        # write your code here        
        l = 0
        r = len(a) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        c1 = r if r >= 0 else 0

        c2 = l if l < len(a) else len(a) - 1

        return c1 if abs(a[c1] - target) <= abs(a[c2] - target) else c2