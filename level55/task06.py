class TreeNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Exemplo de uso:
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# result = search(root, 15)
# print(result.key if result else "Not found")