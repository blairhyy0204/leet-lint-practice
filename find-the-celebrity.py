"""
Leetcode 277. Find the Celebrity
Link: https://leetcode.com/problems/find-the-celebrity

Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Notes: based on the definition of a celebrity, there's at most 1 celebrity in a group.

        # init the candidate to be the first person
        can = 0

        # eliminate 
        for other in range(1, n):
            # can is not a celebrity
            if knows(can, other) or not knows(other, can):
                can = other
            

        for i in range(n):
            if i == can:
                continue

            # check if it is not a celebrity
            if knows(can, i) or not knows(i, can):
                return -1

        return can
            
            