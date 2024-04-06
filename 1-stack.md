
# Stack

## Introduction

A **stack** is a simple datastructure designed around the FILO principle, which means "First In, Last Out". A good analogy for a stack is a pez dispenser, if you are familiar with the candy.


### Uses

Stacks are widely used in various applications, such as:
- Managing function calls in programming languages.
- Undo mechanisms in text editors.
- Syntax parsing in compilers.

## Operations

### Push

The push operation adds an element to the top of the stack.

```python
def push(stack, element):
    stack.append(element)
```

### Pop

The pop operation removes and returns the top element of the stack.

```python
def pop(stack):
    if not isEmpty(stack):
        return stack.pop()
    else:
        return "Stack is empty"
```

### Peek

The peek operation returns the top element of the stack without removing it.

```python
def peek(stack):
    if not isEmpty(stack):
        return stack[-1]
    else:
        return "Stack is empty"
```

### Empty

The empty operation checks if the stack is empty.

```python
def isEmpty(stack):
    return len(stack) == 0
```

## Example: Reversing a String

A super awesome example of a stack being an effecient tool is reversing the digits of a number of the characters of a string. Here is a simple example:

```python
def reverse_string(s):
    stack = []
    for char in s:
        push(stack, char)
    reversed_string = ''
    while not isEmpty(stack):
        reversed_string += pop(stack)
    return reversed_string

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
```

## Problem to Solve: Balancing Parentheses

**Task:** Write a function using a stack to check if a given string of parentheses is balanced. A string is balanced if all open parentheses are closed in the correct order.

**Example Input:** "((()))"

**Example Output:** True

**Example Input:** "(()"

**Example Output:** False

Consider implementing this function and then compare your solution with the provided link

[Solution](stack.py)
