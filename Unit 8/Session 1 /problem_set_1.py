# Problem 1: Build a Binary Tree I

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# U - Understand 
# Create a binary tree with a root = 10, left child = 4 and right child = 6 
# M - Match 
# For tree construction problems, we typically need to:

# Understand the TreeNode structure.
# Assign values and children to nodes correctly to build the desired structure.
# 
# P - Plan 
#  Initialize the constructor for the root = 10, constructor for the left node = 4 and constructor for the right node  = 6 
# I - Implement 

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
# print(root.val, root.left.val, root.right.val)

# R - Review
# 
# Trace through your code with the created tree to ensure that each node is connected correctly according to the problem statement. 
# 
# E - Evaluate
# Time Complexity: O(1) because we are just instantiating three nodes and linking them, which involves a constant amount of work.
# Space Complexity: O(1) because the total space used does not scale with input size; it is constant regardless of scenario.     




# Problem 2: 3-Node Sum I

# U - Understand:
# 
# 

# HAPPY CASE 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True
# Explanation: 4 + 6 = 10, which equals the root value

# EDGE CASE 
#   5
#  / \
# 3   3
# Input: root = 5
# Expected Output: False
# Explanation: 4 + 6 = 10, which does not equal to the root value 

# M - Match:
# This is a simple tree value comparison problem where the solution involves checking a condition involving the root and its immediate children 


# P - Plan:
# check if the value of the left node plus the value of the left node is equal to the value of the root note 
# If it is return True   
# Otherwise return False 

# I - Implement: 
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root.left.val + root.right.val == root.val:
        return True
    return False 
# Alternitively, possible:
# def check_tree(root):
#    return root.val == root.left.val + root.right.val 


root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
# print(check_tree(root))

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
# print(check_tree(root))

# R - Review:
# 
# Test the function with the happy case and edge case to ensure it behaves as expected. 
# 
# E - Evaluate:
# 
#  Time Complexity: O(1) because the operation only involves a few comparisons and is independent of the size of the tree.
# Space Complexity: O(1) because no additional space is required beyond the input.




# Problem 3: 3-Node Sum II

# U - Understand:
# The binary tree can have only tree nodes at maximum 
# 

# HAPPY CASE 
#   10
#  /  
# 10  
# Input: root = 10
# Expected Output: True
# Explanation: the left node is equal to true, the right node is none 

# HAPPY CASE
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True
# Explanation: 3 + 2 = 5, which does equal to the root value 

# EDGE CASE
# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False

# EDGE CASE 
# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False


# M - Match:

# This problem is a variation of the tree validation problem, where we check a specific condition related to the node values in a very small tree.


# P - Plan:
# Initialize the left node value and the right node value to be 0, since we do not know if they exist in the begining
# If there is no root:
#   return False
# if the left child exists:
#   assign the left node value to be the value of the left child
# if the right child exists:
#    assign the right node value to be the value of the right child
# If both children present:
#   Compare the root's value with the sum of the left and right children's value 



# I - Implement: 
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False

    left_child_val = 0 
    right_child_val = 0 

    if root.left:
        left_child_val = root.left.val

    if root.right:
        right_child_val = root.right.val 
    
    children_sum = left_child_val + right_child_val
    return root.val == children_sum
    

root = TreeNode(10)
root.left = TreeNode(10)
# print(check_tree(root))

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(2)
# print(check_tree(root))

root = TreeNode(5)
root.right = TreeNode(2)
# print(check_tree(root))

root = TreeNode(None)
# print(check_tree(root))

# R - Review:
# 
# Test all the cases 
# 
# E - Evaluate:
# 
# Time Complexity: O(1) as the function performs a constant amount of work regardless of input size.
# Space Complexity: O(1) because it uses a fixed amount of space. 




# Problem 4: Find Leftmost Node I

# U - Understand:

#HAPPY CASE 
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4
# Explanation: The leftmost node is equal to 4 

# EDGE CASE 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1
# Explanation: The leftmost root root is 1 so return root value 


# M - Match:

# P - Plan:
# Iterative approach 
# If there is no root, return None
# Set the current pointer on the root to current 

# while the root.left in the tree is None, meaning the leftmost node exits :
#   keep traversing the tree to the left
# return the root value, since the pointer is already at the leftmost value 


# I - Implement: 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    
    if not root:
        return None
    
    # for clarity porposes
    current = root  
    
    while current.left:
        current = current.left
    return current.val

    # Alternatively (from the original solution set)
    # if root is None:
    #     return None
    # # Traverse down to the leftmost child
    # current = root
    # while current.left is not None: (more explicit vs falsy check) 
    #     current = current.left
    # return current.val

        #Note: 

    	# Use if root.left is None: when you want to be explicit about 
        # checking for None specifically, which is often preferred in code where clarity is essential, 
        # especially when working with data structures like binary trees.

	    # Use if not root.left: if you are confident that only None or an actual node (non-falsy) will be present. 
        # This form is shorter and can be stylistically preferred when readability remains clear.


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
# print(left_most(root))


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# print(left_most(root))


# R - Review:
# Verify with different test cases to ensure the function correctly identifies the leftmost node even in unbalanced trees.

# E - Evaluate:   
# Time Complexity: O(n) in the worst case where n is the height of the tree, particularly if it is skewed to one side.
# Space Complexity: O(1) as no additional space is used apart from the input tree structure. 





# Problem 5: Find Leftmost Node II

# U - Understand:

#HAPPY CASE 
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4
# Explanation: The leftmost node is equal to 4 

# EDGE CASE 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1
# Explanation: The leftmost root root is 1 so return root value 


# M - Match:

# P - Plan:
# BASE CASE: If not root.left
#   return value of the root 
# RECURSIVE CASE:
#   keep changing pointer to the left until hit the base case 
#   return the leftmost node   
#

# while the root.left in the tree is None, meaning the leftmost node exits :
#   keep traversing the tree to the left
# return the root value, since the pointer is already at the leftmost value 


# I - Implement: 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    
    if root is None:
        return None 

    if not root.left:
        return root.val
    
    #Also works in this case :
    # if root.left is None:
    #     return root.val

    #Note: 

    	# Use if root.left is None: when you want to be explicit about 
        # checking for None specifically, which is often preferred in code where clarity is essential, 
        # especially when working with data structures like binary trees.

	    # Use if not root.left: if you are confident that only None or an actual node (non-falsy) will be present. 
        # This form is shorter and can be stylistically preferred when readability remains clear.
    
    return left_most(root.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
# print(left_most(root))


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# print(left_most(root))


# R - Review:
# Perform a step-by-step verification using test cases, ensuring the function correctly identifies the leftmost node.

# E - Evaluate:   
# Time Complexity: O(n) in the worst case where n is the height of the tree, as it depends on the number of nodes to the leftmost leaf.
# Space Complexity: O(1) if recursion stack space is not considered, as no extra space beyond input is used.
