class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None   
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_rec(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_rec(node.right, data)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
    def print_inorder(self):
        self.inorder(self.root)     


tree = Tree()
elements = [5, 3, 7, 2, 4, 6, 8]
for elem in elements:
    tree.insert(elem)   
tree.print_inorder()  # Output: 2 3 4 5 6 7 8
print()  # For better readability in output    
