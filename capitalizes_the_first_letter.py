"""
[Lint936]Capitalizes The First Letter
Link: https://www.lintcode.com/problem/936/

Given a sentence of English, update the first letter of each word to uppercase.
"""


class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """

    def capitalizes_first(self, s: str) -> str:
        # Method 1: Find corresponding uppercase letter

        # s_list = list(s)
        # for i in range(len(s)):
        #     if (i == 0 or s[i-1] == " ") and s[i] != " ":
        #         s_list[i] = chr(ord(s[i]) - 32)
        # return ''.join(s_list)

        # Method 2: string.capitalize
        # Notes: split(" ") will keep the space in the string

        s_list = s.split(" ")
        s_list = [word.capitalize() for word in s_list]

        return " ".join(s_list)
