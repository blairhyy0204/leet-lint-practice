"""
[Lint53] Reverse Words in a String
Link: https://www.lintcode.com/problem/53

Given an input string, reverse the string word by word.
"""


class Solution:
    """
    @param s: A string
    @return: A string
    """

    def reverse_words(self, s: str) -> str:
        # write your code here
        # Notes: string.split() v.s string.split(" ")

        s = s.strip()  # remove leading and tailing whitespaces
        s_list = s.split()  # treats consecutive whitespaces as one
        return " ".join(s_list[::-1])
