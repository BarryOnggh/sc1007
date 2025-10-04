class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    """ Inserts a node into the BST. """
    if root is None:
        return BSTNode(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
        
    return root

def inorderRecursive(root):
    """ Prints in-order traversal of the BST (Left, Root, Right). """
    if root:
        inorderRecursive(root.left)
        print(root.data, end=" ")
        inorderRecursive(root.right)


def sumOfNonLeafNodes(root):
    """
    Recursively calculates the sum of all nodes that are not leaves.
    A non-leaf node has at least one child (left or right).
    """





    # Base case: if the node is null or a leaf node, it doesn't contribute to the sum.
    if root is None or (root.left is None and root.right is None):
        return 0

    # If the node is a non-leaf node, add its value to the sum of its subtrees.
    return root.data + sumOfNonLeafNodes(root.left) + sumOfNonLeafNodes(root.right)

if __name__ == "__main__":
    root = None
    print("1: Insert an integer into BST")
    print("2: Sum of all non-leaf nodes")
    print("0: Quit")
    
    while True:
        choice = int(input("\nPlease input your choice (1/2/0): "))
        
        if choice == 1:
            value = int(input("Input an integer to insert: "))
            root = insert(root, value)
            # Automatically print in-order traversal after each insertion
            print("In-order traversal: ", end="")
            inorderRecursive(root)
            print()
        elif choice == 2:
            print(f"Sum of non-leaf nodes: {sumOfNonLeafNodes(root)}")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")