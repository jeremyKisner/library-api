import json
from book import Book

class Library:

	@staticmethod
	def get():
		print('Retrieving Library Books...')
		with open('data/data.json', 'r') as data_file:
			data = json.load(data_file)
		return data

	@staticmethod
	def add(books):
		temp = []
		for book in books:
			temp.append(book.__dict__)
		with open('data/data.json', 'w') as data_file:
			json.dump(temp, data_file, indent=4)

	@staticmethod
	def get_books():
		library_books = []
		data = Library.get()
		for item in data:
			library_books.append(Book(item['name'], item['read']))
		print(f'Total books found: {len(library_books)}')
		return library_books

	def get_book(self, request):
		print(f'Searching for library book: {request}')
		for book in self.books:
			if book.get_name().upper() == request.upper():
				print(f'Found book!')
				return book

	@staticmethod
	def update_book_read(request):
		library_books = Library.get_books()
		for library_book in library_books:
			if library_book.get_name().upper() == request.upper():
				print(f'Updating Book read: {request}')
				library_book.set_read()
		Library.add(library_books)

	@staticmethod
	def add_book(request):
		library_book = Book(request, 0)
		library_books = Library.get_books()
		library_books.append(library_book)
		print(library_books)
		Library.add(library_books)
