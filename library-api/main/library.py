import json

class Library:


	def __init__(self):
		self.inventory = self.__load_inventory__()


	def __load_inventory__(self):
		print("loading library inventory")
		with open('./library-api/resources/book_data.json', 'r') as data_file:
			data = json.load(data_file)
		print(f"library inventory loaded, found {len(data)} books")
		return data


	def __backup_inventory__(self):
		print('making backup of library data')
		with open('data/data.json', 'w') as data_file:
			json.dump(self.inventory, data_file, indent=4)


	def get_inventory_by_identifier(self, identifier):
		return [book[identifier] for book in self.get_inventory()]


	def get_inventory(self) -> list:
		return self.inventory


	def add_inventory(self, incoming_books) -> bool:
		print(f"received request to add book {incoming_books}")
		if type(incoming_books) == dict:
			incoming_books = [incoming_books]
		if type(incoming_books) == list:
			for book in incoming_books:
				if book["isbn_13"] not in self.get_inventory_by_identifier("isbn_13"):
					self.inventory.append(book)
			return True
		return False


	def get_book(self, incoming_book) -> list:
		print(f'searching for library book: {incoming_book}')
		matched_books = []
		if incoming_book:
			for search_term in incoming_book:
				for inventory_item in self.get_inventory():
					if incoming_book[search_term].lower() in inventory_item[search_term].lower():
						matched_books.append(inventory_item)
		print(f"found '{len(matched_books)}' total books matching criteria")
		return matched_books
	

	def delete_book(self, incoming_book_to_delete) -> bool:
		is_deleted = False
		if incoming_book_to_delete:
			books = self.get_inventory()
			for i in range(len(books)):
				if str(incoming_book_to_delete["isbn_13"]) == str(books[i]["isbn_13"]):
					books.pop(i)
					is_deleted = True
					self.inventory = books
					break
		return is_deleted
