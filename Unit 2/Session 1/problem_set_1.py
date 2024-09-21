# Problem 7: Best Book

#U - Understand:
#   Can the list have no dictionaries in it?
#  

#P - Plan 
# In ENGLISH:
# If the list is empty, return None 
# Create a variable for book rating and assign it to the first book rating value in the list 
# Traverse through each dictionary in the list:
# If the current book rating is greater than initial book rating assign the current book rating to be new initial 
# After all books are checked return the dictionary with higher book rating 


# PSEUDOCODE:
# def highest_rated(books):

# if nothing in books:
#   return None 
# highest_rating = books[0]
#
# for each book in books:
#   if the value of the current book rating is larger than the value of first book rating in the list 
#       highest_rating = current book 
# return highest_rating


# I- Implement 
def highest_rated(books):

    if not books:
        return None

    highest_rating_so_far = books[0]
    for book in books[1:]:
        if book["rating"] > highest_rating_so_far["rating"]:
           highest_rating_so_far = book

    return highest_rating_so_far
           


# books = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#     },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#     },
#         {"title": "All Quite on the Western Front",
#      "author": "Remark",
#      "rating": 5.00
#     }
 
# ]



# r = highest_rated(books)
# print(r)

# Problem 8: Index-Value Map

# U - Understand:
# can the list be empty?


# P - Plan:
# In English:

#  if the list is empty return None 
# Initialize new dictionary 
# Initialize current index to be 0 
# for every element in the list
    # add a word as a key and index as a value to the dictionary 
# after the last element has been added to the the dictionary return the completed dictionary. 

# Pseudocode:
# def index_to_value_map(lst):
# index_to_map = {}
# current_index = 0 value for current index 
# for element in list:
#    index_to_map[current_index] = element (0 --> current element of the list)


#I - Implement: 
def index_to_value_map(lst):
    index_val_map = {}
    current_index = 0 

    for element in lst:
        index_val_map[current_index] = element
        current_index += 1 
    return index_val_map

#lst = ["apple", "banana", "cherry", "mango", "pineapple"]
#print(index_to_value_map(lst))
