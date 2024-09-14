# Problem 11: Print the Index

# U - Understand:
# Do we return something when the list is empty?


# P -- Plan: 
# In ENGLISH:
# Iterate over the list of numbers using a range function
# print current index value of each number in a list  


# PSEUDOCODE:
# def print_indices(lst):
#   for index in range(lenght of list):
#       print(index)
#       index + 1 

# I - Implement:
def print_indices(lst):
    for index in range(len(lst)):
        print(index)

# lst = [5,1,3,8,2]
# print_indices(lst)

# Problem 12: Linear Search

# U - Understand:
# Are all of the items in the list are integers?
# Can the list be empty?

# P -- Plan: 
# In ENGLISH:
# iterate over the list of indexes
# if the value at a current index is the same as a target, return that index
# if the value has not been found or a list is empty return -1 


# PSEUDOCODE: 
# def linear_search(lst, target):
#   for index in range of the length of the list:
#       if the  value at the curent index  == the target:
#           return the index
#   return -1 (if the value not found/empty list)

# I - Implement:
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1 

# lst = [1,4,5,2,8]
# position = linear_search(lst,5)
# print(position)


# lst = [1,4,5,2,8]
# position = linear_search(lst,10)
# print(position)

# lst = []
# position = linear_search(lst,10)
# print(position)