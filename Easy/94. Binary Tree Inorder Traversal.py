class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    res = []
    
    def preorder(root):
        if not root:
            return
        
        preorder(root.left)
        res.append(root.val)
        preorder(root.right)
        
    preorder(root)
    return res