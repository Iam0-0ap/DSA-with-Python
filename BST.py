class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
            
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True 


if __name__ == "__main__":
    tree= Node(10)

    # Insert node into the tree
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(11)
    tree.insert(17)
    tree.insert(57)
    tree.insert(16)

    # Inorder Traversal
    tree.inorder_traversal()

    # Pre-order Traversal
    tree.pre_order_traversal()
    
    # Post-order Traversal
    tree.post_order_traversal()

    # Find the node 
    print(tree.find(20))
    print(tree.find(11))