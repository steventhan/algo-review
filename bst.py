from node import TreeNode

def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(preorder(root))
print(postorder(root))