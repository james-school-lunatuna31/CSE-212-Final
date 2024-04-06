class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value: # Recursively find the placement by chopping the search space in half each time.
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def build_bst_and_sort(array):
    if not array:
        return []
    root = None
    for value in array:
        root = insert(root, value)
    return inorder(root)

# Example usage
input_array = [3, 1, 2, 4]
sorted_array = build_bst_and_sort(input_array)
print(sorted_array)
