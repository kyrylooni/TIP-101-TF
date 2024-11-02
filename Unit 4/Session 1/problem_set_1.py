# Problem 1: Prime Number

# U - Understand:
# Can the number be negative
# Prime number is the number:
#   that is greater than 1
#   the number that has two divisors 1 and iself
#   ex: 2 is a price since it's divisor is 1 and 2,
#   ex: 5 is a prime because its divisors are 1 and 5
#   ex: 4 is NOT a prime because its divisiors are 1, 2, 4

# P - Plan:
# In English:
# check if the number is <= 1
#   The number is not a prime
# We know that we are looking in the range from i = 2 to sqrt(n) --> n * n
# Initialize iterator to start at 2 (because our range is from 2 to sqrt(n))
# While current i times itself is less than or equal to n:
# check if n * i does not have any remainder
# return False if there is no remainder
# return True if there is a remainder

# PSEUDOCODE:
# def is_prime(n):
# If n <= 1
#   return false
# iterator_var = 2
# while iterator_var * iterator_var => n:
#  if n  % iterator_var == 0:
#      return False
# iterator_var += 1
# return True


# I - Implement:
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))

# Problem 2: Two-Pointer Reverse List
# U- Understand:
# Can the list be empty?

# P - Plan:
# In English:
# Initialize two pointers left pointer and right
# left pointer is equal to 0 the right ponter is equal to the length of list - 1
# while left pointer is less than the right pointer:
# change the value in the list of the left pointer with the list value of the right pointer value
# add one to the left pointer
# subtract one from the right pointer
# return the reversed list
# Pseudocode:

# I - Implement:
def reverse_list(lst):
    left_pointer = 0
    right_pointer = len(lst) - 1

    while left_pointer < right_pointer:
        temp_variable = lst[left_pointer]
        print("TEMP POINTER:", temp_variable)

        lst[left_pointer] = lst[right_pointer]
        lst[right_pointer] = temp_variable
        # print(lst[left_pointer], lst[right_pointer])
        left_pointer =+ 1
        right_pointer =- 1
    return lst


lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

# Time Complexity:
# O(n), because we iterate over the list once, performing a constant-time swap at each step.
# Space Complexity:
# O(1), because the algorithm uses a fixed amount of extra space (no additional list is created).


# Problem 3: Evaluating Solutions
def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

# Time Complexity:
# O(n) because we are iterating through the list twice (once for slicing and once for copying).
#
# Space Complexity:
# O(n) because we are creating a new list of the same size as the input list.


# Problem 4: Move Even Integers
# U-Understand:
# What if all numbers are even or all odd?
# Should the function sort any numbers either in the even or odd group?

# P-Plan:
# In English:
# Initialize two pointers: 'left' at the start of the list and 'right' at the end of the list
# while 'left' is less than 'right":
#   If the number at 'left' is even, move 'left' pointer one step to the right
#   If number at 'right' is odd, move 'right' pointer one step to the left.
#   If the number at 'left' is odd and the number at 'right' is even, swap them, then move both pointers
# Return the modified list

# I-Implement:

def sort_array_by_parity(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        # Move left pointer forward if current number is even
        if nums[left] % 2 == 0:
            left += 1
        # Move right pointer backward if current number is odd
        elif nums[right] % 2 != 0:
            right -= 1
        # Swap when left pointer points to an odd number and right pointer points to an even number
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


# nums = [3, 1, 2, 4]
# print(sort_array_by_parity(nums))

# Problem 5: Palindrome

# U - Understand:
# The list can be empty, if so,  returns an empty string
# The list may not contain any palindromes, if no palindromes return empty string
# If one word in the list and palindrome, return that word

# P - Plan:
# In English:
# 1) Define a helper function is_palindrome(s):
#   a) Initialize two pointers, left starting at the beginning of the string, and right at the end.
#   b) Loop while left is less than right:
#       i) If characters at left and right are not the same, return False (not a palindrome).
#      ii) Move left pointer one step to the right.
#     iii) Move right pointer one step to the left.
#   c) If no mismatches are found, return True (it is a palindrome).
# 2) Define the main function first_palindrome(words):
#   a) Loop through each word in the list:
#      i) Use the is_palindrome function to check if the current word is a palindrome.
#     ii) If a palindrome is found, return that word immediately.
#   b) If no palindromes are found after checking all words, return an empty string.

# I - Implement:

def is_palindrome(s):

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def first_palindrome(words):
    for word in words:
        if is_palindrome(word):
            return word
    return " "


# alternative version
# def first_palindrome(words):
#     if not words:
#         return " "

#     for word in words:
#         left, right = 0, len(word) - 1
#
#         while left < right:
#             if word[left] != word[right]:
#                 break
#             left += 1
#             right -= 1
#         else:
#             return word
#     return " "


# words = ["abc", "car", "ada", "racecar", "cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc", "racecar", "cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)
