"""
[Lint171] Anagrams
Link:https://www.lintcode.com/problem/171

Given an array of strings, return all groups of strings that are anagrams.If a string is Anagram,there must be another string with the same letter set but different order in S.
"""

from typing import (
    List,
)

# Time Complexity: O(n * k * logk) where n is length of strs and k is the length of each string
# Sorting one string requires k * logk time
# Space Complexity: O(n * k)

# Challenges:
# 1. Hash map key cannot be a list => join the characters to form a new string as the key
# 2. Using one of the anagram as the key takes longer time as comparison is based on the list version of the string and we have to iterate through the keys O(n).
# However, checking the existance of the key requires only O(1)
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
             we will sort your return value in output
    """

    def anagrams(self, strs: List[str]) -> List[str]:
        # write your code here
        count = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in count:
                count[sorted_s].append(s)
            else:
                count[sorted_s] = [s]

        result = []
        for c in count.values():
            if len(c) >= 2:
                result += c

        return result
