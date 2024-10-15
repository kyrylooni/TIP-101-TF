# Problem 1: Pokemon Class

# U - Understand: 
# How do we use the provided class to create an instance?
 

#P - Plan:
# Add a line of code (outside of the class) to instantiate an instance of the class Pokemon 
# and store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu"
# and its types should be ["Electric"].


#I - Implement:
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False


    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self):
        self.is_caught = True 


    def choose(self):
        if self.is_caught == True:
            print(f'{self.name} I choose you!')
        else:
            print(f'{self.name} is wild! Catch them if you can!')

		
        
# my_pokemon = Pokemon("Pikachu", ["Electric"])
# print(my_pokemon.name)
# print(my_pokemon.types)

# Problem 2: Create Squirtle

#U - Understand:
# What steps are necessary to create an instance of a class and use its methods?
#   First, create an instance by providing the required attributes.
#   Second, use the class methods by calling them on the instance.


#P - Plan: 
# Initialize new object squirtle of class pokemon 
# assign attributes for name to be Squirtle and types to be "Water"
# the method print_pokemon of class Pokemon 

#I - Implement:
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

# Problem 3: Is Caught

#U - Understand:
# How do you update an attribute of an object and verify the update?

#P - Plan: 
# Set the `is_caught` attribute of `squirtle` to True to indicate that it has been caught.
# Call the `print_pokemon()` method to print the current state of `squirtle`, verifying the attribute update.


#I - Implement:
squirtle.is_caught = True 
squirtle.print_pokemon()

# Problem 4: Catch Pokemon

# U - Understand: 
# Do we need to modify any of the existing class methods?

#P - Plan: 
# Initialize new method catch, with self attribute only 
# Set is_caught atribute equal to True 


#I - Implement:
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

# Problem 5: Choose Pokemon

# U - Understand: 
# What happens when the choose() method is called on a Pokemon that is not caught?
#   The method should indicate that the Pokemon is still wild.

# P - Plan: 
# Initialize the choose method within a Pokemon class with self attribute only 
# Check if the is_caught attribute set to True,  return "<Pokemon name> I choose you!"
# If the attribute set to False, return "<Pokemon name> is wild! Catch them if you can!" 



#I - Implement:
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
