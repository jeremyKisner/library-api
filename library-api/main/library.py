import json
from main.book import Book

class Library:


	def __init__(self):
		self.inventory = self.load_inventory()
		self.isbn_13 = self.get_isbn_13()


	def load_inventory(self):
		print("loading library inventory")
		with open('./library-api/resources/book_data.json', 'r') as data_file:
			data = json.load(data_file)
		print(f"library inventory loaded, found {len(data)} books")
		return data


	def get_isbn_13(self):
		return [book["isbn-13"] for book in self.get_inventory()]


	def backup_inventory(self):
		print('making backup of library data')
		with open('data/data.json', 'w') as data_file:
			json.dump(self.inventory, data_file, indent=4)


	def get_inventory(self):
		return self.inventory


	def add_inventory(self, incoming_books):
		if type(incoming_books) == dict:
			incoming_books = [incoming_books]
		if type(incoming_books) == list:
			for book in incoming_books:
				pass
			return True
		return False



	# @staticmethod
	# def get_books():
	# 	library_books = []
	# 	data = Library.get_inventory()
	# 	for item in data:
	# 		library_books.append(Book(item['name'], item['read']))
	# 	print(f'Total books found: {len(library_books)}')
	# 	return library_books


	# def get_book(self, request):
	# 	print(f'Searching for library book: {request}')
	# 	for book in self.inventory:
	# 		if book.get_name().upper() == request.upper():
	# 			print(f'Found book!')
	# 			return book


	# @staticmethod
	# def update_book_read(request):
	# 	library_books = Library.get_books()
	# 	for library_book in library_books:
	# 		if library_book.get_name().upper() == request.upper():
	# 			print(f'Updating Book read: {request}')
	# 			library_book.set_read()
	# 	Library.add_books(library_books)


	# @staticmethod
	# def add_book(request):
	# 	library_book = Book(request, 0)
	# 	library_books = Library.get_books()
	# 	library_books.append(library_book)
	# 	print(library_books)
	# 	Library.add_books(library_books)
