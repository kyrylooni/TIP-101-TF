# Problem 14: Multiply List

# U - Understand:
# If the list is empty, what should be returned?
# Does the list have all the positive integers?


# P -- Plan: 
# In ENGLISH:
# initialize a new list 
# iterate over the given list 
# multiply each number by the value of the multiplier 
# append a multiplied number in a new list 
# return new list with multiplied numbers in it

# PSEUDOCODE:   
# def multiply_list(list, multiplier number)
#   new_lst = []
#   for number in lst:
#       mult_num = number * multiplier
#       append new_lst with mult_num 
#   return new_lst

# I - Implement:
def multiply_list(lst, multiplier):
        
    new_lst = []
    for num in lst:
        mult_num = num * multiplier
        new_lst.append(mult_num)
    return new_lst

# lst = []
# new_lst = multiply_list(lst, 3)
# print(new_lst)


# Problem 15: Count Evens

# U - Understand:
# If the list is empty, what should be returned?

# P -- Plan: 
# In ENGLISH:
# Initialize a total evens counter to 0  
# Iterate over the list of numbers 
# Check if very number is even meaning when divisible by two the remainder is 0
# If it is add 1 to the total counter 
# return the total counter 


# PSEUDOCODE:   
# def count_evens(lst):
# total_evens = 0 
# for number in lst:
#   if number % 2 == 0:
#      total_evens += 1 
# return total_evens 

# I - Implement:
def count_evens(lst):
    total_evens = 0
    for num in lst:
        if num % 2 == 0:
            total_evens += 1
    return total_evens
    
# lst1 = [1,5,7,9]
# count1 = count_evens(lst1)
# print(count1)

# lst2 = [2,4,6,8]
# count2 = count_evens(lst2)
# print(count2)