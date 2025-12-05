class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

    def insert(self, data):
        if data < self.value:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.value:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def inorder(self, root):
        res = []
        if root:
            res += self.inorder(root.left)
            res.append(root.value)
            res += self.inorder(root.right)
        return res


# -------- DELETE FUNCTION (तेवढाच extra) --------
def minValueNode(node):
    while node.left:
        node = node.left
    return node

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = deleteNode(root.left, key)

    elif key > root.value:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)

    return root


# ---------------- MAIN ----------------
root = Node(27)
root.insert(14)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(13)
root.insert(20)

print("Tree BEFORE deletion :", root.inorder(root))

key = 14
print("\nDeleting:", key)
root = deleteNode(root, key)

print("Tree AFTER deletion  :", root.inorder(root))
