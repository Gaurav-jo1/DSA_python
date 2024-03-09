class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, data):
        self.root = TreeNode(data)
    
    def insert(self, data, node):
        if data >= node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.insert(data, node.right)
        else:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.insert(data, node.left)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(f"{node.data} ", end="")
            self.preorder_traversal(node.left) 
            self.preorder_traversal(node.right) 

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(3, tree.root)
    tree.insert(7, tree.root)
    tree.insert(2, tree.root)
    tree.insert(4, tree.root)
    tree.insert(6, tree.root)
    tree.insert(8, tree.root)

    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)
    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)
    print("")