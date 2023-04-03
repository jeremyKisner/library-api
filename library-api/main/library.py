import json

import psycopg2
import psycopg2.extras

from database.config import config
from database.create_table import create_tables
from book import Book

class Library:

    def __init__(self):
        self.config = config()
        create_tables(self.config)
        self.books = self.__load_books()
        self.inventory = self.__load_inventory()

    def __load_books(self):
        books = []
        print("loading library inventory")
        conn = psycopg2.connect(**self.config)
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM library;')
        results = cur.fetchall()
        print(results)
        cur.close()
        for result in results:
            books.append(Book(result))
        return books

    def __load_inventory(self):
        with open('./resources/book_data.json', 'r') as data_file:
            data = json.load(data_file)
        print(f"library inventory loaded, found {len(data)} books")
        return data

    def get_inventory_by_identifier(self, identifier):
        return [book[identifier] for book in self.get_inventory()]

    def get_inventory(self) -> list:
        return self.inventory

    def add_inventory(self, incoming_books) -> bool:
        print(f"received request to add book {incoming_books}")
        if type(incoming_books) == dict:
            incoming_books = [incoming_books]
        if type(incoming_books) == list:
            self.add_books(incoming_books)
            for book in incoming_books:
                if book["isbn_13"] not in self.get_inventory_by_identifier("isbn_13"):
                    self.inventory.append(book)
            return True
        return False

    def add_books(self, incoming_books: list) -> bool:
        sql = """INSERT INTO library(name,author,type,isbn_13,isbn_10,published,publisher,copies) 
                VALUES """
        values = [tuple(i.values()) for i in incoming_books]
        try:
            conn = psycopg2.connect(**self.config)
            cur = conn.cursor()
            args = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s)", i).decode('utf-8')
                for i in values)
            cur.execute(sql + args)
            conn.commit()
        except Exception as e:
            print(f"something bad happened {e}")
        finally:
            cur.close()

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
