def balanced_parentheses(s):
	# We need an empty stack to work with
	stack = []

	# While there are many ways to do this, a hash map makes finding the parenthesis in text very easy
	paren_map = {')': '(', '}': '{', ']': '['}

	# Iterate through the charactesr in the list and if the character is an opening character, push to stack. Otherwise, if its a close bracket and it is not in the stack OR the map, then return False. If its a character, skip it.
	for character in s:
		if character in "([{":
			stack.append(character)
		elif char in ")}]":
			if not stack or paren_map[char] != stack.pop():
				return False

	# We are balanced if and only if there is nothing in the stack when we are done.
	return len(stack) == 0