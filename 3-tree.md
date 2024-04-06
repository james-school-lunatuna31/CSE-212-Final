
# Tree

## Introduction

A **tree** is a data structure consisting of nodes, with a single node as the root from which branches lead to child nodes and so on. The structure is designed to represent the relationships between the values in the tree.

## Binary Trees

A special type of tree is the **binary tree**, where each node has at most two children, referred to as the left child and the right child. Binary trees are usually the simplist kind of trees, and we will use them for our examples.

## Operations

### Insertion

Inserting a new node into the binary tree based on some logic (e.g., binary search tree logic, where all left descendents <= n < all right descendents).

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
```

### Deletion

Deleting a node from a binary tree involves three possible scenarios: deleting a leaf node, a node with one child, and a node with two children.

```python
def deleteNode(root, key):
    # Base Case
    if root is None:
        return root
    # Recursive calls for ancestors of node to be deleted
    if key < root.value:
        root.left = deleteNode(root.left, key)
    elif(key > root.value):
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children: Get the inorder successor
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    return root
```

### Searching

Searching for a value in a binary tree can be performed using a simple recursive strategy.

```python
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.value == key:
        return root
    # Key is greater than root's key
    if root.value < key:
        return search(root.right, key)
    # Key is smaller than root's key
    return search(root.left, key)
```

### Traversal

Traversing a tree means visiting all the nodes in the tree. Major tree traversal algorithms include inorder, preorder, and postorder. 

```python
# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

# Preorder traversal
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
```
Here is what each looks like, courtesy of google image search.

![Search](https://1.bp.blogspot.com/-bn3KHYB2BYk/V4OfyZQUnNI/AAAAAAAAGng/T_EEc1IOXEoOdVvFQpCEr-LXAKqyu8F5wCLcB/s1600/binary+tree+PreOrder+traversal+in+Java+.png)
## Example: Building and Traversing a Binary Tree

Creating a binary search tree (BST) and performing various operations including traversal.

```python
root = None
root = insert(root, 8)
insert(root, 3)
insert(root, 10)
insert(root, 1)
insert(root, 6)
insert(root, 14)

print("Inorder traversal of the given tree")
inorder(root)

print("Delete 10")
root = deleteNode(root, 10)
print("Inorder traversal after deletion")
inorder(root)
```

## Problem to Solve: Implement a Tree-Based Sorting Algorithm

**Task:** Implement a function that builds a binary search tree from an array of numbers and then performs an inorder traversal to produce a sorted list.

**Example Input:** [3, 1, 2, 4]

**Example Output:** [1, 2, 3, 4]

Consider implementing this function and then compare your solution with the [provided link](tree.py).
