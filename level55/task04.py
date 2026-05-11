class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    update_height(z)
    update_height(y)
    return y

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    update_height(root)
    
    balance = get_balance(root)
    
    # Caso Esquerda-Esquerda
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    
    # Caso Direita-Direita
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    
    # Caso Esquerda-Direita
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    # Caso Direita-Esquerda
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root