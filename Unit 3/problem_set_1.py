# Problem 1: Calling Mississippi

def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")


# count_mississippi(6)

# Problem 2: Swap Ends

# U - Understand:
# Can the list be empty?

# P - Plan:
# Slice the last letter of the input
# Slice the middle of the string (excluding the first and the last) characters of the input
# Add all three parts together and return the final string


# I - Implement:
def swap_ends(my_str):
    return my_str[-1:] + my_str[1:-1] + my_str[:1]


# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)


# Problem 3: Is Pangram

# U - Understand:
# Can the list be empty?

# P - Plan:
# Initialize the alphabet string to compare letters in the strings
# travers through the input string
# if the curent letter is in the alphabet return true
# else return false


# I - Implement:

def is_pangram(my_str):
    english_characters = "abcdefghijklmnopqrstuvwxyz"

    for char in english_characters:
        if char not in my_str.lower():
            return False
    return True


# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))


# Problem 4: Reverse String

# Understand:
# Can the string be empty?

# Plan:
# Return a slicing of the entire input string, but with a negated step parameter

# Implement:
def reverse_string(my_str):
    return my_str[::-1]


# my_str = "live"
# print(reverse_string(my_str))

# Problem 5: First Unique

# Understand:
# Can the string be empty?

# Plan:
# 1) Initialize the dictionary that will count each index in the string
# 2) Iterate over the input string and add it to the dictionary with the corespondent counter value (1 if seen at least once, increment counter on each character)
# 3) Loop through each character of the input string again, but also track the current index
#   a) If that character occurs once, return the current index
# 4) If no character with value 1 is found in the dictionary, return -1


# Implement:


def first_unique_char(my_str):

    count_dict = {}

    for char in my_str:
        count_dict[char] = count_dict.get(char, 0) + 1

    for index, char in enumerate(my_str):
        if count_dict[char] == 1:
            return index
    return - 1


# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))
