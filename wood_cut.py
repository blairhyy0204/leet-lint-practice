"""
[LintCode 183]Wood Cut
Link: https://www.lintcode.com/problem/183

Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
"""

from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def get_num_logs(self, l: List[int], length: int):
        result = 0
        for i in l:
            result += i // length
        return result

    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        if len(l) == 0:
            return 0

        max_len = sum(l) // k
        min_len = max(l) // k

        while min_len <= max_len:
            mid = min_len + (max_len - min_len) // 2
            if mid == 0 or self.get_num_logs(l, mid) >= k:
                min_len = mid + 1
            else:
                max_len = mid - 1
            
        return max_len