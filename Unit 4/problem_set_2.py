# Problem 1: Merge Sorted Lists (Problem set 2 unintentionally, but still useful :) )

# U - Understand:
# Can the lists be empty?
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
