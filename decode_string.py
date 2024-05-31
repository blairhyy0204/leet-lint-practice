"""
[Leet394] Decode String
Link: https://leetcode.com/problems/decode-string

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        dig = []

        for i in s:
            if i != "]":
                dig.append(i)
            else :
                cur = ""
                while dig[-1] != "[":
                    cur = dig.pop() + cur
                dig.pop() # pop "["
                n = ""
                while dig and dig[-1].isdigit():
                    n = dig.pop() + n
                cur = cur * int(n)
                dig.append(cur) # stack back constructed substr
        
        return "".join(dig)