"""
[Lint415] Valid Palindrome
Link: https://www.lintcode.com/problem/415

Given a string, determine if it is a palindrome, only letters and numbers are considered and case is ignored

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"

Example 2:
Input: "race a car"
Output: false
Explanation: "raceacar"

Example 3:
输入: "1b , 1"
输出: true
解释: "1b1"
"""

# Space: O(1)
# Time: O(n)
# Notes: str.isdigit() checks if it is number. str.isalpha() checks if it is letter
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if not (s[i].isdigit() or s[i].isalpha()):
                i += 1
                continue

            if not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True
