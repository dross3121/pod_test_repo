

'''
Object-oriented book challenge! 

Your challenge for today is to complete the fill out the missing parts of the Booklist class in book_class.py
Then, test each method for the class Booklist!

Hint: all methods for the Booklist class go in the book_class.py script
This class and the methods are already imported in this script -- test them here for specific cases!
'''

# import the Booklist class and corresponding methods
import numpy as np
from book_class import *


'''
PART #1. 
Set up the initialization function for class Booklist()
The function should initialize just 1 attribute, called 'books', as an empty list
No parameters needed, other than self

Then, create an object of class Booklist called 'my_library' in this script.
Finally, print the books attribute of my_library -- it should be an empty list
Also, print out the type of my_library to see what you get :) 
'''

my_library = Booklist()
print(my_library.books)

   





'''
Part #2: 
Define the add() method to add a book to an object of class Booklist
-The method should take 2 parameters other than self, both strings -- 'title', and 'author'
-The method should make a book variable as a dictionary with two key/value pairs for title/author
-Then, the method should append this book to books attribute of the the Booklist object  - i.e. self.books.append(book)

Once you have finished the method, add the following books to your booklist:
Just Mercy - Bryan Stevenson
The New Jim Crow - Michelle Alexander
The Truths We Hold - Kamala Harris
My Grandmother's Hands - Resmaa Menakem

Finally, print the books attribute of my_library to make sure your books have been added!
'''

my_library.add("Bryan Stevenson","Just Mercy")
my_library.add("Michelle Alexander","The New Jim Crow")
my_library.add("Kamala Harris","The Truths We Hold")
my_library.add("Resmaa Menakem","My Grandmother's Hands")
print(my_library.books)




# Part #3: 
# Define the count_books() method to get the number of books in an object of class Booklist
# -the method only needs the self parameter
# -the method should return an integer that is the length of the list stored in the books attribute

# Once you have finished the method, count the books in my_library and print out the result
# '''
# print('\nPart 3\n')

my_library.count_books()

'''
Part #4: 
Define the remove_title() method which will remove a book by its title from an objectof class Booklist
-the method should take the self parameter, plus an additional paramter 'title' (a string for the title of the book to remove)
-the method should remove any books matching the input title from the Booklist
-it does not need to return anything

Once you have finished the method, remove 'Just Mercy' from my_library
Then, print out the books attribute to make sure that book is gone
'''
my_library.remove_title("Just Mercy")



'''
Part #5:
Instantiate another object of class Booklist called nyt_bestsellers
Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
You can find NYT books here: https://www.nytimes.com/books/best-sellers/

Then, print out the books attribute of nyt_bestsellers
'''


nyc_bestsellers = Booklist()
nyc_bestsellers.add("Amor Towles", "The Lincoln Highway")
nyc_bestsellers.add("The Wish", "NIcholas Sparks")
print(nyc_bestsellers.books)



