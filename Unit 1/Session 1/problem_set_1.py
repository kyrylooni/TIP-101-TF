# Problem 14: Total Sum in Range 


# U - Understand:
    # If the range is in negative numbers (start and stop both negative), what should be returned?
    # If the star value is larger than stop value 


# P -- Plan: 
# In ENGLISH:
# If the range starts with a negative value return 0, since we cant add the negative value 
# Initialize total
# Loop over the range of the numbers from start value up to and including the last stop value in the range
# Accumulate the total by adding each number to it on each iteration
# Once the for loop reaches the stop value return total 
# 
# 
# PSEUDOCODE:
# def sum_range(start, stop):
# if the start < 0, meaning start from negative return 0, assuming we can only add positive integers 
# initialize total = 0 
# for each number in range(start up to and including stop value)
#   total = total + number 
# return the total in the range 

# I - Implement:
def sum_range(start, stop):
    if start < 0: # base
        return 0 
    total = 0 
    
    for num in range(start, stop + 1):
        total += num
    return total
    
# Problem 15: Negative Numbers

# U - Understand:
    # What if the list of integers is empty what should be returned?
    # Is there only negative numbers?

# P -- Plan:
# Check if the list is empty return 0 
# Iterate over the list of given integers 
# check if the each number is less than 0, then print it 


# PSEUDOCODE:   
# def print_negatives(lst):
# if the length of the list < 0:
#   return 0 
# for each number in lst:
# if number < 0:
#   print a negative number


# I - Implement:
def print_negatives(lst):
    if len(lst) < 0:
        return 0 
    
    for num in lst:
        if num < 0:
            print(num)
       
       
# print_negatives([3,-2,2,1,-5])

