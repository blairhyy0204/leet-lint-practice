"""
[LintCode 462] Total Occurrence of Target
Link: https://www.lintcode.com/problem/462/

Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.
"""

from typing import (
    List,
)


class Solution:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def total_occurrence(self, a: List[int], target: int) -> int:
        # write your code here
        if not a:
            return 0

        l = 0
        r = len(a) - 1

        while l + 1 < r:
            mid = l + (r - l) // 2
            if a[mid] < target:
                l = mid
            else:
                r = mid

        if a[l] == target:
            head = l
        elif a[r] == target:
            head = r
        else:
            return 0

        l = 0
        r = len(a) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if a[mid] <= target:
                l = mid
            else:
                r = mid

        if a[r] == target:
            tail = r
        elif a[l] == target:
            tail = l
        else:
            return 0

        return tail - head + 1
