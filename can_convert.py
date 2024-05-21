"""
[LintCode1540] Can Convert
Link: https://www.lintcode.com/problem/1540/

Given two string S and T, determine if S can be changed to T by deleting some letters (including 0 letter)

Example1
Input: S = "lintcode" and T = "lint"
Output: true

Example2
Input: S = "lintcode" and T = "ide"
Output: true

Example3
Input: S = "adda" and T = "aad"
Output: false
Explanation: You can not change "adda" to "aad" by deleting one 'd'.
"""

# Space: O(1)
# Time: O(n)
class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def can_convert(self, s: str, t: str) -> bool:
        if s == None or len(s) < len(t):
            return False

        # Two pointers
        p2 = 0

        for i in range(len(s)):
            if s[i] == t[p2]:
                p2 += 1
                if p2 >= len(t):
                    return True
                    
        return False