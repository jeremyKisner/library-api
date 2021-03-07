import json
from book import Book

class Library:

	def get():
		""" returns the library data """
		print('Retrieving Library Books...')
		with open('data/data.json', 'r') as data_file:
			data = data_file.read()
		books = []
		for book in json.loads(data):
			books.append(Book(book['name'], book['read']))
		print(f'Total books found: {len(books)}')
		return books

	def get_book(request):
		""" returns the book found """
		print(f'Searching for library book: {request}')
		for library_book in Library.get():
			if library_book.name.upper() in request.upper():
				print('Library book found!')
				return library_book

	def update_book_read(library_book):
		book = Library.get_book(library_book)
		print(f'Updating Book read: {book.name}')
		book.set_read()
