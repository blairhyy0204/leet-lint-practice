"""
[Lint1352] Compare Version Numbers
Link: https://www.lintcode.com/problem/1352

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
"""

# Time Complexity: O(max(n, m))
# Space Complexity: O(m+n)
class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """

    def compare_version(self, version1: str, version2: str) -> int:
        # Write your code here
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        v1_n = len(v1_list)
        v2_n = len(v2_list)

        for i in range(max(v1_n, v2_n)):
            if i >= v1_n:
                v1_list[i] = 0
            elif i >= v2_n:
                v2_list[i] = 0

            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            elif int(v2_list[i]) > int(v1_list[i]):
                return -1

        return 0
