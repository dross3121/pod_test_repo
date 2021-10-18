class Booklist():
	def __init__(self):
		self.books = books = []
	
	def add(self, author, title):
		book={}
		book["author"] = author
		book["title"] = title
		self.books.append(book)
		
	def count_books(self):
		print(len(self.books))

	def remove_title(self,title):
		self.title = str(title)
		for book in self.books:
			if book['title'] == self.title:
				self.books.remove(book)
				print(self.books)
		
	# 	for book in books_with_details:
    # if book['author'] == author:
    #   authors_books.append(book['title'])
		
	
	
	# def display_titles(self, author, title, books):
	# 	pass

# print(Booklist.books)
 


