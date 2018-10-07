class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        strings = []
        cur = self
        while cur:
            strings.append(str(cur.val))
            cur = cur.next
        return "->".join(strings)


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}".format(self.val)
