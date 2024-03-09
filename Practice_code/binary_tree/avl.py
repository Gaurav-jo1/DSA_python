# 1. Create a AVL Node
class AVLNode():
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        return str(self.key)

class AVLTree():
    def __init__(self) -> None:
        self.root = None

    # 2. Insert the Key
    def insert(self, key, node):
        if not node:
            return AVLNode(key)
        elif key > node.key:
            node.right = self.insert(key, node.right)
        else:
            node.left = self.insert(key, node.left)

        # 3. Assign the height
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 4. Check the balance of tree
        balance = self.balance(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)


        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        # 5. Rotate the tree
        return node
    
    def insert_key(self, key):
        self.root = self.insert(key, self.root)
        return self.root
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance(self, node):
        if not node:
            return 0
        
        return self.height(node.left) - self.height(node.right)
    

# Example usage:
avl_tree = AVLTree()
avl_tree.insert_key(10)
avl_tree.insert_key(20)
avl_tree.insert_key(30)
avl_tree.insert_key(40)
avl_tree.insert_key(25)