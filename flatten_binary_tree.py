# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = [root]

        while stack:
            popped = stack.pop()
            print("1", popped.val)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)
            if len(stack) > 0:
                print(stack[-1].val)
