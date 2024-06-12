"""
[LintCode 75] Find Peak Element
Link: https://www.lintcode.com/problem/75

There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1]
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        l = 1
        r = len(a) - 2

        while l <= r:
            mid = l + (r-l) // 2

            # if value @ mid > mid + 1, contract the right bound
            if a[mid] > a[mid+1]:
                r = mid - 1
            else:
                l = mid + 1

        return l