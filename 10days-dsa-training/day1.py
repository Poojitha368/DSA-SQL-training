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
    # def inorder(self, node):
    #     if node:
    #         self.inorder(node.left)
    #         print(node.data, end=' ')
    #         self.inorder(node.right)
    # def print_inorder(self):
    #     self.inorder(self.root)     
    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        '''queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result'''
        queue = [self.root]
        level_size = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
                

    def level_order_traversal_snake(self):
        if self.root == None:
            return []
        result = []
        queue = []
        level_size = 0
        left_to_right = True
        queue.append(self.root)
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                result.append(node.data)
                if left_to_right == True:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
            left_to_right = not(left_to_right)
        return result
    # def least_common_ansestor(self,node1,node2):
        # pass
        


tree = Tree()
elements = [5, 3, 7, 2, 4, 6, 8]
for elem in elements:
    tree.insert(elem)   
   
print(tree.level_order_traversal())
print(tree.level_order_traversal_snake())
