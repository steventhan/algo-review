class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t: return True
        if (s.val == t.val and self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)):
            print("1 ", s.val, t.val)
            return True

        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            print("2 ", s.val, t.val)
            return True
        return False
