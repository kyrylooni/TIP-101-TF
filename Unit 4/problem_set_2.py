# Problem 1: Merge Sorted Lists (Problem set 2 unintentionally, but still useful :) )

# U - Understand:
# Can one of the list the list be empty?
# What if the lists are different sizes
# Needs to implement same direction pointer of two-pointer approach

# P - Plan:
# In English:
# Initialize a new empty merged list
# Initialize the pointer for the first list
# Initialize the pointer for the second list
# While pointer for the first list is less then the length of the first list
# and the second pointer is less then the length of the second list:
#   If the the value of the pointer list 1 is smaller than the the value of the pointer list 2:
#       Append the value from the list 1 to the new merged list
#       Increment the list 1 pointer
#   else:
#       Append the value fron the list 2 to the new merged list
#       Increment the list 2 pointers
#
# Once one list is exhausted, append the remaining elements of the other list to `merged list`.
# Return merged list

# I - Implement:
def merge_sorted_lists(lst1, lst2):
    merge_lst = []

    lst1_pointer = 0
    lst2_pointer = 0

    while lst1_pointer < len(lst1) and lst2_pointer < len(lst2):
        if lst1[lst1_pointer] < lst2[lst2_pointer]:
            merge_lst.append(lst1[lst1_pointer])
            lst1_pointer += 1
        else:
            merge_lst.append(lst2[lst2_pointer])
            lst2_pointer += 1

    while lst1_pointer < len(lst1):
        merge_lst.append(lst1[lst1_pointer])
        lst1_pointer += 1

    while lst2_pointer < len(lst2):
        merge_lst.append(lst2[lst2_pointer])
        lst2_pointer += 1

    return merge_lst


# lst1 = [1, 3, 5]
# lst2 = [2, 4, 6]
# merged_lst = merge_sorted_lists(lst1, lst2)
# print(merged_lst)

# Problem 1: Long Pressed

# U-Understand:
# Needs to implement same direction pointer of two-pointer approach


# P-Plan:
# In English:
# Initialize name pointer and set it to 0
# Initialize typed pointer and set it to 0
# While typed pointer is less than the length of typed:
#   If name pointer is less than the length of name and current character of name is the same as the curent character of typed string
#       Increment the name pointer
#       Increment the typed pointer
#   Else if the typed pointer is greater than 0 and the value of the current pointer is equal to the value at the previous position of the pointer
#       Increment the type pointer
#   Else
#       return False (it is not a long-press)
# return the chheck name pointer is equal to the length of name


# I-Implement
def is_long_pressed(name, typed):
    name_pointer = 0
    typed_pointer = 0

    while typed_pointer < len(typed):
        if name_pointer < len(name) and name[name_pointer] == typed[typed_pointer]:
            # If the characters match, move both pointers
            name_pointer += 1
            typed_pointer += 1
        elif typed_pointer > 0 and typed[typed_pointer] == typed[typed_pointer - 1]:
            # If the current character in 'typed' matches the previous character,
            # it means it was long-pressed, so only move 'typed_pointer'
            typed_pointer += 1
        else:
            # If there's no match and it's not a long-press, return False
            return False

    # After processing all characters in 'typed', ensure that all characters in 'name' were matched
    return name_pointer == len(name)


name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
