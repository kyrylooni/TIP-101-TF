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

#

# M - Match:

# P - Plan:

# I - Implement:

def sum_list(lst):
    pass

# R- Review:
#  
# E - Evaluate: 
#   