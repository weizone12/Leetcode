class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root: TreeNode):
    res = []
    
    def preorder(root):
        if not root:
            return
        
        res.append("(")
        res.append(str(root.val))
        
        if not root.left and root.right:
            res.append("()")
        preorder(root.left)
        preorder(root.right)
        
        res.append(")")
        
    preorder(root)
    return "".join(res)[1:-1]