class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    if not root:
        return 0
    return root.height

def rightRotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def getBalance(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = getBalance(root)

    # LL
    if balance > 1 and key < root.left.key:
        return rightRotate(root)
    # RR
    if balance < -1 and key > root.right.key:
        return leftRotate(root)
    # LR
    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # RL
    if balance < -1 and key < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

root = None
nums = [10, 20, 30, 40, 50, 25]
for num in nums:
    root = insert(root, num)

print("Preorder Traversal of AVL Tree:")
preorder(root)
