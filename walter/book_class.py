class Booklist():
	def __init__(self):
		# Initializing the books attribute
		self.books = []

	def add(self, title, author):
		# Creating empty dictionary, assigning ke/value pair inside dict.  Then appending dictionary to books list attribute.
		book = {}
		book["title"] = title
		book["author"] = author
		self.books.append(book)

	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		pass

	def display_titles(self):
		pass

	print('PART 1\n')
my_library = Booklist()
print(my_library.books)
print(type(my_library))



