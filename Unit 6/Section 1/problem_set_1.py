# Problem 1: Nested Constructors
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	


# U - Understand:
 
# P - Plan:
# Initialize a chained constructor call to create a linked list 4 -> 3 -> 2
# Start by working inside-out creating the last node 2 
# Then initialize the node with value 3 and link it to the last node of value 2 (3->2) 
# At thne end initialize the head node of value 4 and ;ink it to the middle node of value 3 (4 -> 3)

# I - Implement:
head = Node(4, Node(3, Node(2)))
# print(head.value, "->", head.next.value, "->", head.next.next.value)

# Problem 2: Find Frequency

# U - Understand:
# Q: How should the function handle an empty linked list?
	# A: The function should return 0 if the linked list is empty since there would be no instances of the value.

# HAPPY CASE
# Input: [1, 2, 3, 4, 3, 3], 3
# Output: 3
# Explanation: The value 3 appears three times in the linked list.

# EDGE CASE
# Input: [], 5
# Output: 0
# Explanation: The linked list is empty, so the frequency of any value is 0.

# M - Match 
	# For Linked List problems, we want to consider the following approaches:

	# Traverse the list while counting occurrences of a specific value.
	# Use a simple iterative method to handle each node until the end is reached.


# P - Plan 
	# Start with the head of the list 
	# Initialize counter to 0 
	# Interate the list:
	# 	If the curent node value is the same as the target value
	#		Increment the counter 
	# 	Move the pointer to the next node 
	# Return the counter value after traversing the entire list

# I - Implement 
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
          
	def count_element(head, val):
		count = 0 
		current = head

		while current:
			if current.value == val:
				count += 1 
			current = current.next
		return count




# R - Review 
	# Trace through your code with an input to check for the expected output
	# Catch possible edge cases and off-by-one errors

# E - Evaluate
# 	Assume N represents the number of nodes in the linked list.
# 		Time Complexity: O(N) because we need to traverse each node in the linked list to check for the value.
# 		Space Complexity: O(1) because we use only a fixed amount of space regardless of the input size. 

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1

# bin_lst = Node(3, Node(1, Node(2, Node (1))))
# head, val = 3, 1  

# bin_lst.count_element(head, val)

# Problem 3: Remove Tail

#U - Understand:
# What should the output be when the linked list is empty or contains only one element?
# 	The function should return None as there is no tail to remove, which indicates an empty list.

	# HAPPY CASE
	# Input: head = Node(1, Node(2, Node(3, Node(4))))
	# Output: 1 -> 2 -> 3
	# Explanation: The tail node with value 4 is successfully removed, leaving the list correctly adjusted.

	# EDGE CASE
	# Input: head = Node(1)
	# Output: None
	# Explanation: Removing the tail from a single-node list should result in an empty list, returned as `None`.

#M - Match:

#	This problem revolves around bug identification and correction in a singly linked list operation, a common issue in data structure manipulation.

#P - Plan:

# 1) Print the current `node`'s value before moving to the next to ensure we are not already at the last node.
# 2) Add print statements before altering the next pointer to confirm the correct node is modified.
# 3) Fix the bug by adjusting the loop condition to stop at the second-to-last node!

#I - Implement 
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next:  # Stop at the second-to-last node
        print(f"Current Node: {current.value} -> Next Node: {current.next.value}")
        current = current.next
    print(f"Removing tail node with value: {current.next.value}")
    current.next = None
    return head

head = Node(1, Node(2, Node(3, Node(4))))
print("Before removing:")
print_list(head)
remove_tail(head)
print("After removing:")
print_list(head)

#R - Review:
	# Test with a multi-node list to ensure the last node is removed correctly.
	# Test with a single node to confirm the function handles it without errors.
      
# E- Evaluate:
	# Time Complexity: O(N) because we traverse the linked list up to the second-to-last node.
	# Space Complexity: O(1) because the space usage does not increase with the size of the input.
