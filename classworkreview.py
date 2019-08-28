# # Python classes review graded
#
# ### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
#
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
#
# Remember, this is the basic model of a Python file with a class
# ```
# class Movie:
#     def __init__(self):
#     # Class constructor code and property handling
#
#     OTHER PROPERTIES AND METHODS HERE
#
# def main():
# # Create class instance(s) and perform other activities in/from this function
# }
#
# main()
# ```
#
class Movie:
    #initial instances of each property in the class
    def __init__(self, movieName, rating, yearReleased):
        self.movieName = movieName
        self.rating = rating
        self.yearReleased = yearReleased
    #STR overides the output in the console which only shows the storage space in computer memory returning all of what was placed in the f-string
    def __str__(self):
        return f'{self.movieName}, {self.rating}, {self.yearReleased}'

# ### Problem 2:
# Create a class Product that represents a product sold online.
#
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes
# of the Product class
#
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.

class Product:
    #initial instances of each property in the class
    def __init__(self, price, quantity, name):
        self.price = price
        self.quantity = quantity
        self.name = name

    #STR overides the output in the console which only shows the storage space in computer memory returning all of what was placed in the f-string
    def __str__(self):
        return f'${self.price}, {self.quantity}, {self.name}'
def main():
    #initiates instances of my classes
    favoriteMovie = Movie("Braddock", "PG-16", "1988")
    print(favoriteMovie) #prints current properties that are stored in the instances
    newProduct = Product("12.00", "1", "Dress")
    print(newProduct) #prints current properties that are stored in the instances
    newProduct1 =Product("24.00", "2", "Pants")
    print(newProduct1)
main()
