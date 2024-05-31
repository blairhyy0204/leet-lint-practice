"""
[Lint494] Implement Stack by Two Queues
Link: https://www.lintcode.com/problem/494

Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.
"""

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    # loop through a queue and find the last item 
    # move other items to another queue for temporary storage
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        # write your code here
        self.q1.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        x =  self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1
        return x
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.q1) != 0:
            x = self.q1.pop(0)
            self.q2.append(x)
        self.q1, self.q2 = self.q2, self.q1
        return x
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.q1) == 0
