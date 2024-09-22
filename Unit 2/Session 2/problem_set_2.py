# Problem 6: How Many Smaller

# U - Understand:
# Can the list be empty?
# Can the list have anything other than integers?

# P - Plan:
# In ENGLISH:(Pseudocode)
# Create a sorted copy of the nums list
# Create an empty dict to store value : smaller counts.
# For each index in nums
#   If the value at index is not in our dict, map value -> index
#   Otherwise, skip, as this is a duplicate of a value we've already checked
# Create an empty list to store the results in their original order
# For each number in the original list (not sorted list)
#   Use the dict to lookup the count for that number
#   Add that count value to our results list
# Return the results list


# I- Implement:
def smallerNumbersThanCurrent(nums):
    # Sort the nums list
    sorted_nums = sorted(nums)

    # Dictionary to store the smallest index at which each number appears
    smaller_count_map = {}
    for i in range(len(sorted_nums)):
        num = sorted_nums[i]
        # Only set the index for the first occurrence of each number
        if num not in smaller_count_map:
            smaller_count_map[num] = i

    # Manually generate the result based on the original list values
    result = []
    for num in nums:
        result.append(smaller_count_map[num])

    return result

# Problem 7: Good Pairs

# U - Understand:
# Why does i < j matter?

# P - Plan:
# In ENGLISH:(Pseudocode)
# First, create a frequency map for the list
# Create a variable to hold pairs, initialized to 0
# For each value in our frequency map:
#   Calculate the possible pairs for that value
#   Add the possible pairs to our pairs variable
# Return the total number of pairs

# I- Implement:


def numIdenticalPairs(nums):
    frequency_map = {}
    good_pairs = 0

    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for count in frequency_map.values():
        good_pairs += count * (count - 1) // 2

    return good_pairs


# nums = [1, 2, 3, 1, 1, 3]
# ans = numIdenticalPairs(nums)
# print(ans)
