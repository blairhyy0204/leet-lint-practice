"""
[Lint40] Implement Queue by Two Stacks
Link: https://www.lintcode.com/problem/40/

As the title described, you should only use two stacks to implement a queue's actions.
The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.
Both pop and top methods should return the value of first element.
"""

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        result = self.s1.pop()

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        return result
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.s1) != 0:
            x = self.s1.pop()
            self.s2.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        return x