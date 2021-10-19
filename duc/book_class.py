
# Part 1

class Booklist():
	def __init__(self):
		self.books = []

# Part 2

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)

# Part 3

	def count_books(self):
		return(len(self.books))

# Part 4		

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)		

#Part 6
	def display_titles(self):
		titles = []






