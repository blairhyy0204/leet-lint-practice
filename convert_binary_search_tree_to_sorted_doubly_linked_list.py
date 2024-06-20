"""
[LeetCode 426]Convert Binary Search Tree to Sorted Doubly Linked List
Link: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    # def traverse(self, root):
    def __init__(self):
        self.dummy = Node(val=-1)
        self.p = self.dummy

    def traverse(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            self.p.right = Node(val=root.val, left=self.p)
            self.p = self.p.right
            return

        self.traverse(root.left)
        self.p.right = Node(val=root.val, left=self.p)
        self.p = self.p.right
        self.traverse(root.right) 

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return 
            
        self.traverse(root)
        self.p.right = self.dummy.right
        self.dummy.right.left = self.p
        return self.dummy.right