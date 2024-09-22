# Problem 6: Has Duplicates

# U - Understand:
# Can nums be empty?


# P - Plan:
# In ENGLISH:
# Create an empty dictionary to track recent indices
# For index in nums
#   If the value is already in recent dict, compare indices
#       If the index - recent index <= k,
#           we found a valid duplicate and can return True
#   Update the dict with current index
# If nothing is found return false


# I- Implement:
def hasDuplicates(nums, k):
    recent_index = {}
    for i in range(len(nums)):
        if nums[i] in recent_index:
            diff = i - recent_index[nums[i]]
            if diff <= k:
                return True
        recent_index[nums[i]] = i
    return False


# Problem 7: Make Pairs

# U - Understand:
# Can nums be empty?
# Can there be an odd number of entries in the list?


# P - Plan:
# In ENGLISH:(Pseudocode)
# Create an empty dictionary to count all occurences of each number in the list
# Traverse through the list of num
#   add each occurence to the dictionary
# For every value in the dictionary
#   If the value is not evenly divisible by 2
#       return False
# Otherwise, return True

# I- Implement:
def divideList(nums):
    frequency_dict = {}

    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    for count in frequency_dict.values():
        if count % 2 != 0:
            return False  # odd count of frequencies, cnnot be divided into pairs

    return True  # even count of frequencies, can be divided into pairs.
