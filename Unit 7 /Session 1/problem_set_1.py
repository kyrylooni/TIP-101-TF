# Problem 1: Hello Hello

# U - Understand:

#

# M - Match:

# P - Plan:

# I - Implement:
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
# repeat_hello(5)
# R- Review:
#  
# E - Evaluate: 
#   



# Problem 2: Factorial Cases

# U - Understand:
# 
# HAPPY CASE
# Input: 5
# Output: 120
# Explanation: The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

# EDGE CASE
# Input: 0
# Output: 1
# Explanation: The factorial of 0 is defined as 1.
# M - Match:
# Direct recursive function calls implementing the mathematical definition of factorial.
# Consideration of special cases like the factorial of 0. 

# P - Plan:
    # 1) Base Case: If `n` is 0, return 1 (since 0! = 1).
    # 2) Recursive Case: Return `n * factorial(n - 1)`.
# I - Implement:
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)

print(factorial(5))

# R- Review:
#   Trace through your code with an input of 5 to ensure each recursive call is calculated correctly and aggregates to 120.
#   Validate the base case with input 0, which should return 1 directly.
# E - Evaluate: 
#   Time Complexity: O(n) because we make n recursive calls.
#   Space Complexity: O(n) because each recursive call adds a layer to the call stack, using more memory.


# Problem 3: Recursive Sum

# U - Understand:
# HAPPY CASE
# Input: [1, 2, 3, 4, 5]
# Output: sum = 15 
# Explanation: The sum of the elements in the list is 1 + 2 + 3 + 4 + 5 = 15:

# EDGE CASE
# Input: []
# Output: sum = 0 
# Explanation: Since the list is empty return the sum will be 0, there is nothing to add 

# M - Match:
# Breaking down the problem into smaller parts by considering one element at a time.
# Using recursion to sum the rest of the list.

# P - Plan:
# Base case: When list is empty, the sum is equal to 0
# Recursive case: Return the first element of the list plus the result of a recursive call to `sum_list()` with the rest of the list.
# Each recursive call will take a smaller version of the original list, moving toward the base case, removing the first element each time 

# I - Implement:

def sum_list(lst):
	if len(lst) == 0:
		return 0 
	else:
		return lst[0] + sum_list(lst[1:])

lst = [1, 2, 3, 4, 5]
print(sum_list(lst))

        
# R- Review:
# Trace through your code with an input of [1, 2, 3, 4, 5] to check that each element is added correctly, resulting in 15.
# Ensure that passing an empty list results in 0, correctly handling the edge case.

#  
# E - Evaluate: 
#  Time Complexity: O(n) because we need to process each element in the list once.
# Space Complexity: O(n) due to the recursion stack depth being proportional to the list size.
