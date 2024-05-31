"""
[lint 423] Valid Parentheses
Link: https://www.lintcode.com/problem/423/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        # use stack data structure
        parentheses_dict = {")": "(", "}": "{", "]": "["}

        memo = []
        for i in s:
            if i in parentheses_dict:
                if len(memo) == 0 or memo[-1] != parentheses_dict[i]:
                    return False
                memo.pop()
            else: 
                memo.append(i)

        return len(memo) == 0