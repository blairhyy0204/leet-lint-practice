"""
[Leet224] Basic Calculator
Link: https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
"""


class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        # Write your code here
        stack = []
        for i in s:
            if i != ")":
                if i != " ":
                    stack.append(i)
            else:
                num = 0
                k = ""
                while stack[-1] != "(":
                    val = stack.pop()
                    if val == "+":
                        num += int(k)
                        k = ""
                    elif val == "-":
                        num -= int(k)
                        k = ""
                    else:
                        k = val + k
                num += int(k)
                stack.pop() # pop "("

                stack.append(str(num))

        result = 0
        k = ""
        while len(stack) > 1:
            val = stack.pop()
            if val == "+":
                result += int(k)
                k = ""
            elif val == "-":
                result -= int(k)
                k = ""
            elif val.isdigit():
                k = val + k
        
        result += int(stack.pop())
        return result
