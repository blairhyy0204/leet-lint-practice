"""
[LintCode 60] Search Insert Position
Link: https://www.lintcode.com/problem/60/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume NO duplicates in the array.
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def search_insert(self, a: List[int], target: int) -> int:
        # write your code here

        l = 0
        r = len(a) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                l = mid + 1
            elif a[mid] > target:
                r = mid - 1

        # find the smallest number larger than target, which has the index to insert into
        return l
            
