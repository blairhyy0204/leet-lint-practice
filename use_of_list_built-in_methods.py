"""
[LintCode2128]Use of list built-in methods
Link: https://www.lintcode.com/problem/2128/

Please refine the code in solution.py to implement the following functions.

get_len: return the length of the input list
get_max: return the maximum value of the elements of the input list
get_min: returns the smallest element of the input list
pop_list: returns the result of the input list after the last element value has been removed
Each of these functions has only one argument list_in.

We will import your code from solution.py in main.py and run it. If your code is logically correct and runs successfully, the program will return a list as the result of the operation.he result.
"""


def get_len(list_in: list) -> int:
    """
    :param list_in: The first input list
    :return: The length of the list_in
    """
    # write your code here
    return len(list_in)


def get_max(list_in: list) -> int:
    """
    :param list_in: The first input list
    :return: The largest value of list_in
    """
    # write your code here
    return max(list_in)


def get_min(list_in: list) -> int:
    """
    :param list_in: The first input list
    :return: The smallest value of list_in
    """
    # write your code here
    return min(list_in)


def pop_list(list_in: list) -> list:
    """
    :param tuple_in: The first input tuple
    :return: The list delete the last element
    """
    # write your code here
    return list_in[:-1]
