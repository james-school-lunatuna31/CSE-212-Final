
# Linked List

## Introduction

Linked lists are specialized data structures that connect data to other data in a linear fashion. They are similar to arrays, but are dynamically sized whilst still maintaining quick insertion, deletion, or edits to individual elements.

## Types of Linked Lists

- **Singly Linked Lists:** Each node points to the next node in the list and the last node points to null. These are commonly used in dynamic arrays.
- **Doubly Linked Lists:** Each node has two links, one to the next node and another to the previous node. These are especially helpful when the list is performing navigation (such as a browser history + a back button)
- **Circular Linked Lists:** Similar to singly or doubly linked lists, but the last node points back to the first node, forming a circle. These can be helpful for music playlists, slideshows, or anything that needs to continously cycle.

## Operations

### Insertion

Inserting a new node to the linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
```

### Deletion

Deleting a node from the linked list.

```python
    def delete(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None
```

### Searching

Searching for an element in the linked list.

```python
    def search(self, key):
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        return False
```

## Example: Creating a Singly Linked List

Implementing a singly linked list in Python and performing basic operations such as insert and delete.

```python
# Creating a singly linked list and adding elements
llist = LinkedList()
llist.insert(3)
llist.insert(2)
llist.insert(1)
print("Created linked list is:")
llist.printList()

# Deleting a node from the linked list
llist.delete(2)
print("Linked list after deletion:")
llist.printList()
```

## Problem to Solve: Reversing a Linked List

**Task:** Write a function to reverse a singly linked list.

**Example Input:** 1 -> 2 -> 3 -> None

**Example Output:** 3 -> 2 -> 1 -> None

Consider implementing this function and then compare your solution with the (provided link)[linkList.py]

## Overhead and Time Complexity
### Overhead

**Arrays**
While linked lists may seem more powerful than arrays in many ways, there are a few major differences (especially in lower level languages). Arrays require a static memory size, so you have to know how big they are when they are created. Changing the size of them requires creating a new array every single time. The benefit of though is a simple allocation of memory, which is very fast.

**Linked Lists**
Linked lists require much more expensive memory operations as every single node requires memory being allocated, sometime s more than once (doubley linked lists). As a result, usage of linked lists can impact the memory performance of your computer over statically sized arrays.


A good rule of thumb is to always use an array if you know the size of the list when writing the code AND you know that the list size will not need to change very often.

### Time Complexity
The great power of the dynamic list does not come for free, and usage of linked lists can signifigantly impact performance of a program if not used carefully. To give an idea, here is a comparison to a typical array:

**Access**

*Array*: O(1) - Since the elements in an array are literally just a block of contiguous memory, we can access them in constant time.

*Linked Lists*: O(n) - To access an element, we have to start at the head or the tail and follow the links. Sometimes we can improve this with binary search IF the elements are sorted on insert, but that also has a cost associated with it. Seriously large linked lists can take signifigant time to iterate over.

**Insertion/Deletion**

*Arrays*: 

 1. Start of List: O(n)
 2. Middle of List: O(n)
 3. End of List: O(1) or O(n)

If we insert at the start of an array, we have to shift every element over by one. Consquently, we must visit every single element and move its reference before assigning it to the new array. When inserting at the end, if we have space we can just do it. However, like before, if we need to re-size the array, we must copy every element which requires visiting every element. For the middle of the list, like the start, requires splicing the array and moving data. The worst case scenario for doing this requires iterating over nearly all of the data, and is thus O(n).

*Linked Lists*

 1. Start of List: O(1)
 2. Middle of List: O(n)
 3. End of List: O(1) or O(n)

With linekd lists, the data is encpasulated into the nodes, so we don't have to move around as much to insert items. If inserting at the start of the list, it is as simple as setting the new node as the head. That's it. For the middle of the last, it is the same as an array because we might need to visit every element to find the nodes to insert off of. For the end of the list, we must iterate over every item to get to the last element unless it is a doubley linked list, which is O(1) since we can use the tail pointer.

Overall, Linked Lists are more expensive than arrays, but can be useful when dealing with data that needs stored dynamically or require the order of the list to change frequently.