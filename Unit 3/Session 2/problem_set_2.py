# Problem 1: Sum of Strings

# U - Understand:
# Can the list be empty?

# P - Plan:
# Initialize the total sum variable to be 0
# Traverse through the list of nums and convert each string to an integer
# Add the current number to the total sum variable

# I - Implement:
def sum_of_number_strings(nums):
    total_sum = 0
    for num in nums:
        total_sum += int(num)
    return total_sum


# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)


# Problem 2: Remove Duplicates

# U - Understand:
# Can the list be empty

# P - Plan:
# Check if the list is empty, return an empty list
# Initialize the the no duplicates list to have a first element from nums.
# Initialize the i counter to start from the second element
# while current counter is less than the lenght of nums
#   if the current value in the list does not equal the previous one
#       add the value to no duplicates list
#   increment the counter by 1
# return no duplicates list

# I - Implement:
def remove_duplicates(nums):
    if not nums:  # Check for an empty list
        return []

    no_dups = [nums[0]]  # Initialize with the first element
    i = 1  # Start from the second element

    while i < len(nums):
        if nums[i] != nums[i - 1]:  # Compare current element with the previous one
            no_dups.append(nums[i])
        i += 1  # Move to the next element

    return no_dups


# nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
# print(remove_duplicates(nums))

# Problem 3: Reverse Letters
# U - Understand:
# What will the function output?

# P - Plan:

# 1) Create an empty list for the letters
# 2) Loop through the string, and add any letters to the list
# 3) Make an index variable, set to end of letters list
# 4) Create an empty results string
# 5) Loop through each character in the original string
#   a) If the char was a letter:
#      i) add the value at letters[index] to results
#     ii) reduce index by 1
#   b) Otherwise, add the char itself to results
# 6) Return results

# I - Implement:

def reverse_only_letters(s):
    letters = []  # Collect letters
    for c in s:
        if c.isalpha():
            letters.append(c)

    result = ""
    letters_index = len(letters) - 1  # Start from the end of the letters list

    for c in s:
        if c.isalpha():
            result += letters[letters_index]
            letters_index -= 1
        else:
            result += c
    return result


# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

# Problem 4: Longest Uniform Substring
# U - Understand:
# Will the string ever be empty?

# P - Plan
# 1) If the input string is empty, return 0
# 2) Set a variable to track the largest uniform substring and the current uniform substring
# 3) Loop through the length of the input string
#   a) If the current and previous characters are equal, increase the current uniform substring counter and update the largest uniform
#      substring counter
#   b) Otherwise, reset the current uniform substring counter to 1
# 4) Return the largest uniform substring counter

# I - Implement
def longest_uniform_substring(s):
    if not s:
        return 0
    max_length = 1
    current_length = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length


# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)

# Problem 5: Teemo's Attack

# U - Understand:
# If Teemo attack while Ashe is still poisoned, does the attack second towards the duration?

# P - Plan:
# 1) Create an empty variable for total poisoned duration
# 2) For each attack time except the last one
#   a) Actual duration is the smaller of:
#       - the duration input
#       - the next attack time minus this attack time
#   b) Add the actual duration to the total
# 3) The last attack will always fully complete,
#    so add one more duration to the total
# 4) Return total

# I - Implement:
def find_poisoned_duration(time_series, duration):
    total_duration = 0
    for i in range(len(time_series)-1):
        # Calculate the actual poisoning time between two attacks
        actual_duration = min(time_series[i+1] - time_series[i] - 1, duration)

        total_duration += actual_duration
    # Add the duration of the last attack
    total_duration += duration
    return total_duration


time_series = [1, 4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage)
