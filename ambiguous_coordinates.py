"""
[Lint1372] Ambiguous Coordinates
Link: https://www.lintcode.com/problem/1372

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces, and ended up with the string S. Return a list of strings representing all possibilities for what our original coordinates could have been.
Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits. Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".
The final answer list can be returned in any order. Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)
"""
from typing import (
    List,
)

# Time Complexity: O(n^3)
# Space Complexisty: O(n^3)
class Solution:
    """
    @param s: An string
    @return: An string
             we will sort your return value in output
    """

    def helper(self, a: str) -> List[str]:
        a_list = []

        for point in range(len(a)):
            num_digits_before_point = point + 1
            num_digits_after_point = len(a) - num_digits_before_point

            # check digits before decimal
            if num_digits_before_point > 1 and int(a[0]) == 0:
                continue
            elif num_digits_after_point > 0 and int(a[-1]) == 0:
                continue
            else:
                if point != len(a) - 1:
                    a_list.append(
                        a[:num_digits_before_point] + "." + a[num_digits_before_point:]
                    )
                else:
                    a_list.append(a)
        return a_list

    def ambiguous_coordinates(self, s: str) -> List[str]:
        # write your code here
        result = []
        s = s[1:-1]
        for comma in range(1, len(s)):
            a = s[:comma]
            b = s[comma:]
            a_list = self.helper(a)
            b_list = self.helper(b)

            for i in a_list:
                for j in b_list:
                    result.append(f"({i}, {j})")

        return result
