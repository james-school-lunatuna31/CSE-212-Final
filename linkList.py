class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Temporarily save the next node
        current.next = prev  # Reverse the current node's next value
        prev = current  # Move prev node to current
        current = next_node  # Move to the next node
    return prev  # make previous the head of the list

# Usage
head = ListNode(1, ListNode(2, ListNode(3)))
print("Original list:")
print_list(head)

reversed_list_head = reverse_linked_list(head)
print("Reversed list:")
print_list(reversed_list_head)
