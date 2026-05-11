class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search_bst(root: TreeNode, val: int) -> TreeNode:
    if root is None or root.value == val:
        return root
    if val < root.value:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)