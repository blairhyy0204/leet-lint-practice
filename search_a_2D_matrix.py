"""
[LintCode 28]Search a 2D Matrix
Link: https://www.lintcode.com/problem/28/

Write an efficient algorithm that searches for a target value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        # find the row
        n_row = len(matrix) 
        n_column = len(matrix[0]) 

        l = 0 
        r = n_row - 1

        while l <= r:
            mid = l + (r-l) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1

        row = r

        # find the column
        l = 0 
        r = n_column - 1

        while l <= r:
            mid = l + (r-l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1

        return False