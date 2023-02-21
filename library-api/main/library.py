import json
# from main.book import Book

class Library:


	def __init__(self):
		self.inventory = self.__load_inventory__()


	def __load_inventory__(self):
		print("loading library inventory")
		with open('./library-api/resources/book_data.json', 'r') as data_file:
			data = json.load(data_file)
		print(f"library inventory loaded, found {len(data)} books")
		return data


	def get_inventory_by_identifier(self, identifier):
		return [book[identifier] for book in self.get_inventory()]


	def __backup_inventory__(self):
		print('making backup of library data')
		with open('data/data.json', 'w') as data_file:
			json.dump(self.inventory, data_file, indent=4)


	def get_inventory(self) -> list:
		return self.inventory


	def add_inventory(self, incoming_books) -> bool:
		if type(incoming_books) == dict:
			incoming_books = [incoming_books]
		if type(incoming_books) == list:
			for book in incoming_books:
				if book["isbn-13"] not in self.get_inventory_by_identifier("isbn-13"):
					self.inventory.append(book)
			return True
		return False


	def get_book(self, incoming_book) -> list:
		print(f'Searching for library book: {incoming_book}')
		matched_books = []
		if incoming_book:
			for search_term in incoming_book:
				for inventory_item in self.get_inventory():
					if incoming_book[search_term].lower() in inventory_item[search_term].lower():
						matched_books.append(inventory_item)
		print("found '{len(matched_books)}' total books matching criteria")
		return matched_books


	# @staticmethod
	# def update_book_read(request):
	# 	library_books = Library.get_books()
	# 	for library_book in library_books:
	# 		if library_book.get_name().upper() == request.upper():
	# 			print(f'Updating Book read: {request}')
	# 			library_book.set_read()
	# 	Library.add_books(library_books)
