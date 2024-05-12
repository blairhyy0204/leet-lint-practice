"""
[LintCode2314]List modification, addition and deletion of elements
Link: https://www.lintcode.com/problem/2314/

This problem has a list list_1. We need you to refine the code in solution.py to do the following.

modify the element in the third position of the index of the list list_1 to be 1999.
add an element 'jiuzhang' to the list list_1.
delete the first element of the list list_1.
We will import the code you refined in solution.py in main.py and run it. If your code is logically correct and runs successfully, the program will output list_1 with the changed elements.ents.
"""


def list_update_del(list_1: list) -> list:
    """
    :param list_1:  the source list
    :return: modified list_1
    """
    # --write your code here--
    list_1[2] = 1999
    list_1.append("jiuzhang")
    list_1.pop(0)
