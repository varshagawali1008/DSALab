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

    def preorder(self, root):
        res = []
        if root:
            res.append(root.value)
            res += self.preorder(root.left)
            res += self.preorder(root.right)
        return res

    def postorder(self, root):
        res = []
        if root:
            res += self.postorder(root.left)
            res += self.postorder(root.right)
            res.append(root.value)
        return res

root = Node(27)
root.insert(14)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(13)
root.insert(20)

print("Inorder Traversal  :", root.inorder(root))
print("Preorder Traversal :", root.preorder(root))
print("Postorder Traversal:", root.postorder(root))
