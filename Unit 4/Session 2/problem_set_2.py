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


# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))


# Problem 2: Sharing Cookies

# U - Understand:
# What should the function return if there are no cookies or no children?
#   The function should return 0, as no children can be made content without cookies.
# How does the function handle large numbers and potentially large inputs?
#   The function will work as long as it operates within Python's handling of large lists and sorts them efficiently.


# P - Plan:
# In English:
# Sort the list of greed factors and the list of cookie sizes.
# Initialize pointers for children (child_i) and cookies (cookie_j)
# While there are still children and cookies:
#   Check if the current smallest cookie can satisfy the current child's greed.
#       If it can, move to the next child
#   Move to the next cookie regardless of whether it satisfied a child's greed or not.
# Return the count of content children, indicated by the child index pointer.


# I - Implement:
def find_content_children(g, s):
    g.sort()  # Sort the greed factors
    s.sort()  # Sort the sizes of the cookies
    child_i, cookie_j = 0, 0
    while child_i < len(g) and cookie_j < len(s):
        if g[child_i] <= s[cookie_j]:
            # This child can be content with this cookie, move to next child
            child_i += 1
        # Move to next cookie whether it was used to content a child or not
        cookie_j += 1
    return child_i


# g = [1, 2, 3]
# s = [1, 1, 3]
# print(find_content_children(s, g))

# g1 = [1, 1]
# s1 = [2, 2, 2]
# print(find_content_children(s1, g1))


# Problem 3: Valid Palindrome

# U - Understand:
# What happens if the input string is empty?
    # The function should return True, as an empty string or a string with a single character is trivially a palindrome.
# How does the function handle case sensitivity and non-alphanumeric characters?
    # Assuming standard palindrome conditions where only alphanumeric characters are considered and they are case insensitive.
    # However, this specific implementation does not address these issues and treats the string as is.


# P - Plan:
# In English:
# 1) Start with two pointers at the beginning and end of the string.
# 2) While the two pointers haven't met:
#   a) If characters at the pointers match, move both pointers towards the center.
#   b) If they don't match:
#      i) Check if skipping the character at the left pointer results in a palindrome.
#     ii) Check if skipping the character at the right pointer results in a palindrome.
#     iii) Return True if either of the above checks returns True.
# 3) Return True if no mismatches were severe enough to prevent a palindrome (after considering one removal).


# I - Implement:
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True


def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # When characters mismatch, check the two possibilities
        if s[left] != s[right]:
            # Check by skipping left character or skipping right character
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left, right = left + 1, right - 1

    # If it's already a palindrome or can be one by removing a character
    return True


s = "aba"
s2 = "abca"
s3 = "abc"

# print(valid_palindrome(s))
# print(valid_palindrome(s2))
# print(valid_palindrome(s3))
