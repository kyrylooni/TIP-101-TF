# Problem 7: Best Movie Genre

#U - Understand:
# Can two movies have the same genre?

#P - Plan 
# In ENGLISH:
# Create a dictionary for ratings 
# Create a dictionary for counts 
# Traverse through each movie 
# If genre already in both dicts 
#   Add the movie's rating to that genre's rating total 
#   Add 1 to the genre's movie total 
# Otherwise add the rating as a new entry and set count to 1 

# Highest avg rating starts at 0
# Loop through each genre
#   Calculate the average using the ratings and counts for that genre
#   If the avg is higher, make new highest avg
# Return the name of the highest avg genre

# I- Implement:
def most_popular_genre(movies):
    
    genre_ratings = {}
    genre_counts = {}
    for movie in movies:
        curr_genre = movie['genre']
        if curr_genre not in genre_ratings:
            genre_ratings[curr_genre] = movie['rating']
            genre_counts[curr_genre] = 1
        else:
            genre_ratings[curr_genre] += movie['rating']
            genre_counts[curr_genre] += 1

    highest_avg_rating = 0
    most_popular = None
    for genre in genre_ratings:
        avg_rating = genre_ratings[genre] / genre_counts[genre]
        if avg_rating > highest_avg_rating:
            highest_avg_rating = avg_rating
            most_popular = genre

    return most_popular



# Problem 8: Quality Control
# U - Understand:


#P - Plan 
# In ENGLISH:
# Initialize a new dictionary for pass/fail for product id as a key and determined score as a value 
# Traverse the dictionary 
# If current score is greater than or equal to threshold add the product id as a key and "pass" as a value to pass_fail dictionary 
# If current score is less than to threshold add the product id as a key and "fail" as a value to pass_fail dictionary 
# At the end return pass_fail dictionary 


# I- Implement:
def quality_control(product_scores, threshold):
    pass_fail_dict = {}

    for id in product_scores:
        if product_scores[id] >= threshold:
            pass_fail_dict[id] = "pass"
        else:
            pass_fail_dict[id] = "fail"
    return pass_fail_dict



# scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
# threshold = 60

# print(quality_control(scores, threshold))