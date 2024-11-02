# Problem 1: Neatly Nested
# U - Understand:

# HAPPY CASE
# Input: "(())"
# Output: True
# Explanation: The string is a correctly nested pair of parentheses.

# EDGE CASE
# Input: "(()"
# Output: False
# Explanation: The string has an unmatched opening parenthesis.

# M - Match:

# Using recursion to simplify the validation of nested structures.

# P - Plan:

# 1) If the string is empty, return True (base case).
# 2) If the string starts with '(' and ends with ')', recursively validate the substring between them.
# 3) Otherwise, return False.

# I - Implement:

def is_nested_parens(s):
    if s == "":
        return True
    if len(s) >= 2 and s[0] == '(' and s[-1] == ')':
        return is_nested_parens(s[1:-1])
    return False
		
# R- Review:

# Test the function with input "(())" to ensure it returns True.
# Validate with input "(()" and ensure it returns False, correctly handling the edge case
  
# E - Evaluate: 

# Time Complexity: O(n) because each recursive call processes two fewer characters until the string is empty or invalid.
# Space Complexity: O(n) due to the recursion stack depth, potentially extending to the length of the string in deeply nested cases.
 
# Problem 2: How Many 1s
# U - Understand:

# HAPPY CASE
# Input: [0, 0, 0, 1, 1, 1, 1]
# Output: 4
# Explanation: There are four 1's in the array.

# EDGE CASE
# Input: [0, 0, 0, 0, 0]
# Output: 0
# Explanation: There are no 1's in the array.


# M - Match:

# Utilizing binary search to minimize the number of elements inspected, which is particularly useful when dealing with large datasets.

# P - Plan:

# 1) If the last element of the array is 0, return 0.
# 2) Use binary search to find the first occurrence of 1.
# 3) If 1 is found, subtract its index from the length of the array to get the count of 1's.
# 4) If no 1 is found during the search, return 0.

# I - Implement:

def count_ones(lst):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1
    
    # Check if low is within the array bounds and points to a 1
    if low < len(lst) and lst[low] == 1:
        return len(lst) - low
    return 0
		
# R- Review:

# Test the function with inputs like [0, 0, 0, 1, 1, 1, 1] to ensure it returns 4.
# Check with an input of [0, 0, 0, 0, 0] to confirm that it correctly identifies the absence of 1's.
  
# E - Evaluate: 

# Time Complexity: O(log n) due to the binary search approach.
# Space Complexity: O(1) as it requires constant space regardless of the input size.

# Problem 3: Binary Search IV
# U - Understand:

# HAPPY CASE
# Input: nums = [1, 3, 5, 7, 9], target = 5
# Output: 2
# Explanation: The target value 5 exists in the list at index 2.

# EDGE CASE
# Input: nums = [1, 3, 5, 7, 9], target = 2
# Output: -1
# Explanation: The target value 2 does not exist in the list.

# M - Match:

# Understanding the fundamental properties of binary search.
# Implementing it in a recursive fashion, which is a common approach in algorithmic problem-solving.

# P - Plan:

# 1) Base Case: If the range is exhausted without finding the target, return -1.
# 2) Calculate the middle index of the current search range.
# 3) If the middle element is the target, return its index.
# 4) If the target is less than the middle element, recursively search the left half.
# 5) If the target is greater than the middle element, recursively search the right half.

# I - Implement:

def binary_search(nums, left, right, target):
    if left > right:
        return -1  # Target is not found

    mid = (left + right) // 2
    
    # Found the target, return its index.
    if nums[mid] == target:
        return mid
    
    # Decide to search left or right half.
    if target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, right, target)

def binary_search_recursive(nums, target):
    # Initial call to the external binary search function
    return binary_search(nums, 0, len(nums) - 1, target)
		
# R- Review:

# Trace through your code with a list [1, 3, 5, 7, 9] and a target of 5 to ensure it correctly identifies index 2.
# Validate with a target not in the list (e.g., 2) to check that it returns -1, correctly handling the edge case.
  
# E - Evaluate: 

# Time Complexity: O(log n) because each recursive call reduces the problem size by half.
# Space Complexity: O(log n) due to the recursion depth being equal to the logarithm of the list size.

# Problem 4: Count Rotations
# U - Understand:

# HAPPY CASE
# Input: [11, 12, 15, 18, 2, 5, 6, 8]
# Output: 4
# Explanation: The array has been rotated 4 times (the minimum element, 2, is at index 4).

# EDGE CASE
# Input: [2, 5, 6, 8, 11, 12, 15, 18]
# Output: 0
# Explanation: The array is not rotated (the minimum element is at index 0).

# M - Match:

# Adapting binary search to find the point of minimum value, which indicates the number of rotations.

# P - Plan:

# 1) Establish pointers for the beginning (`low`) and end (`high`) of the array.
# 2) If the element at `low` is less than or equal to the element at `high`, the array is not rotated.
# 3) Use a loop to continue searching as long as `low` is less than `high`:
#    - Calculate the middle index (`mid`).
#    - Check the relationship between `mid`, `low`, and `high` to determine the unsorted part:
#      - If the element at `mid` is greater than the element at `high`, the rotation is in the right half, set `low` to `mid + 1`.
#      - Otherwise, set `high` to `mid`.
# 4) At the end of the loop, `low` will point to the smallest element, which is the number of rotations.

# I - Implement:

def count_rotations(nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        if nums[low] <= nums[high]:  # Array is sorted, no rotation
            return low
        mid = (low + high) // 2
        next_index = (mid + 1) % len(nums)  # circular indexing
        prev_index = (mid - 1 + len(nums)) % len(nums)  # circular indexing
        
        # Check if the mid element is the minimum element
        if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
            return mid
        elif nums[mid] > nums[high]:
            low = mid + 1  # Min must be in the right unsorted portion
        else:
            high = mid - 1  # Min must be in the left unsorted portion

    return 0  # This return is technically unreachable due to the logic
		
# R- Review:

# Test the function with input [11, 12, 15, 18, 2, 5, 6, 8] to ensure it returns 4.
# Validate with a non-rotated input [2, 5, 6, 8, 11, 12, 15, 18] to confirm that it correctly identifies 0 rotations.
  
# E - Evaluate:

# Time Complexity: O(log n) because each iteration of the loop narrows the search range by about half.
# Space Complexity: O(1) as it uses a constant amount of space.

# Problem 5: Merge Sort I

# U - Understand:

# HAPPY CASE
# Input: [5,3,8,6,2,7,1,4]
# Output: [1,2,3,4,5,6,7,8]
# Explanation: The list is sorted in ascending order.

# EDGE CASE
# Input: [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: The merge sort should handle arrays of identical elements without changing their order.


# M - Match:

# Using recursion to divide the problem into smaller parts, sort each part, and then merge them back together.

# P - Plan:

# 1) If the list length is 0 or 1, it is already sorted, so return it.
# 2) Split the list into two halves.
# 3) Recursively apply merge sort to both halves.
# 4) Merge the two sorted halves into a single sorted list using the merge function.
# 5) Return the merged and sorted list.

# I - Implement:

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)
    
def merge(left, right):
    result = [] 
    i = j = 0  
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result
		
# R- Review:

# Test with input [5,3,8,6,2,7,1,4] to ensure it sorts correctly to [1,2,3,4,5,6,7,8].
# Check with an array of identical elements [1,1,1,1] to confirm correct handling.

  
# E - Evaluate: 

#   