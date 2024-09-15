#Problem 11: Odd Indices

# U - Understand:
# Can the list be empty?

# P -- Plan: 
# In ENGLISH:
# Iterate over the range of indecies 
# If index is odd meaning the division by 2 produces a remainder 
# Print a value at that odd index

# PSEUDOCODE:
# def print_odd_indices(nums):
# for each index in the range of length of a list 
    # if index % 2 != 0 produces a remainder
        # print(nums[index])


# I - Implement:
def print_odd_indices(nums):
    for i in range(len(nums)):
        if i % 2 != 0:
            print(nums[i])

# nums = [3,4,8,1,5,2]
# print_odd_indices(nums)

# Problem 12: List Occurrences

# U - Understand:
# Can the list be empty?
# Can list include anything other than integer values?

# P -- Plan: 
# In ENGLISH:
# Initialize new list for indices that will match the target 
# Iterate over the range of indecies
# If the value at the current index matches the target value, append that to the new indices list 
# Return the appended list 

# PSEUDOCODE:
# def find_all_occurrences(lst, target):
# new_idx_lst = []
# for each index in the range of length of a list:
#   if list[index] == target 
#       new_idx_lst.append(index)
# return new_idx_lst


# I - Implement:
def find_all_occurrences(lst, target):
    new_idx_lst = []

    for i in range(len(lst)):
        if lst[i] == target:
            new_idx_lst.append(i)
    return new_idx_lst

# lst = [1,2,6,5,2,1,3,2,2]
# index_list = find_all_occurrences(lst, 2)
# print(index_list)
