"""
[Lint812] Bold Words in String
Link: https://www.lintcode.com/problem/812/

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

Example
Example 1:
Input:
["ab", "bc"]
"aabcd"
Output:
"a<b>abc</b>d"

Example 2:
Input:
["bcccaeb","b","eedcbda","aeebebebd","ccd","eabbbdcde","deaaea","aea","accebbb","d"]
"ceaaabbbedabbecbcced"
Output:
"ceaaa<b>bbb</b>e<b>d</b>a<b>bb</b>ec<b>b</b>cce<b>d</b>"
"""

from typing import (
    List,
)


class Solution:
    """
    @param words: the words
    @param s: the string
    @return: the string with least number of tags
    """

    def bold_words(self, words: List[str], s: str) -> str:
        # Write your code here
        n = len(s)
        highlight = [False] * n
        print(highlight)

        for i in range(len(s)):
            for w in words:
                w_length = len(w)
                if s[i : i + w_length] == w:
                    highlight[i : i + w_length] = [True] * w_length

        result = ""
        in_tag = False
        for i in range(len(s)):
            if highlight[i] == False and in_tag == True:
                result += f"</b>{s[i]}"
                in_tag = False
            elif highlight[i] == True and in_tag == False:
                result += f"<b>{s[i]}"
                in_tag = True
            else:
                result += s[i]

        if in_tag:
            result += "</b>"

        return result
