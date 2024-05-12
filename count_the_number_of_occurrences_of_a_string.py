"""
[LintCode 2395]Count the number of occurrences of a string
Link: https://www.lintcode.com/problem/2395/

In this question, we will provide a string str_1. We have already declared the count_string function for you in solution.py. The initial str_1 of this function represents the initial string. You need to do:

Count the number of occurrences of the character a in the string;
Count the number of times the character going is in the range of the string 0 to 40.
"""


def count_string(str_1: str) -> tuple:
    """
    :param str_1: Input string
    :return: Count the number of occurrences of a string
    """
    # -- write your code here --
    return str_1.count("a"), str_1[:40].count("going")
