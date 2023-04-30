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

    def __load_books(self):
        print("loading library inventory")
        conn = psycopg2.connect(**self.config)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM library;')
        results = cur.fetchall()
        print(results)
        cur.close()
        books = []
        for row in results:
            books.append(dict(row))
        return books

    def get_books(self) -> list:
        return self.books

    def add_books(self, incoming_books: list) -> bool:
        print(f"received request to add book {incoming_books}")
        if isinstance(incoming_books, dict):
            incoming_books = [incoming_books]
        if isinstance(incoming_books, list):
            try:
                conn = psycopg2.connect(**self.config)
                cur = conn.cursor()
                for book in incoming_books:
                    book = Book(book)
                    sql = """INSERT INTO library(name,author,type,isbn_13,isbn_10,published,publisher,copies) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    cur.execute(sql, book.get())
                    conn.commit()
                self.books = self.__load_books()
                return True
            except Exception as e:
                print(f"something bad happened {e}")
                raise e
            finally:
                cur.close()
        return False

    def get_matching_books(self, incoming_book) -> list:
        print(f'searching for library book: {incoming_book}')
        matched_books = []
        if incoming_book:
            for search_term in incoming_book:
                for inventory_item in self.get_books():
                    if str(incoming_book[search_term]).lower() in str(inventory_item[search_term]).lower():
                        matched_books.append(inventory_item)
        print(f"found '{len(matched_books)}' total books matching criteria")
        return matched_books
    
    def get_book_by_id(self, incoming_book) -> dict:
        print(f'searching for library book: {incoming_book}')
        matched_book = {}
        if incoming_book:
            for search_term in incoming_book:
                for inventory_item in self.get_books():
                    if str(incoming_book[search_term]).lower() == str(inventory_item[search_term]).lower():
                        matched_book = inventory_item
        return matched_book

    def delete_book(self, incoming_book_to_delete: dict) -> bool:
        is_deleted = False
        if incoming_book_to_delete:
            for i in range(len(self.get_books())):
                params = ""
                for param in incoming_book_to_delete:
                    if not params:
                        params += f"{param}={incoming_book_to_delete[param]}"
                    else:
                        params += f" AND {param}={incoming_book_to_delete[param]}"
                if params:
                    conn = psycopg2.connect(**self.config)
                    cur = conn.cursor()
                    sql = """ DELETE FROM library WHERE """
                    cur.execute(sql + params)
                    rows_deleted = cur.rowcount
                    conn.commit()
                    cur.close()
                    print(f'rows deleted {rows_deleted}')
                    self.get_books().pop(i)
                    is_deleted = True
                    self.books = self.__load_books()
                    break
        return is_deleted

    def check_out(self, incoming_book):
        is_checked_out = False
        print(f"received request to checkout book {incoming_book}")
        _book = self.get_book_by_id({"library_id": incoming_book})
        if _book and _book["copies"] > 0:
            is_checked_out = True
        if is_checked_out:
            print("updating record")
            conn = psycopg2.connect(**self.config)
            cur = conn.cursor()
            sql = """ UPDATE library SET copies=%s WHERE library_id=%s """
            cur.execute(sql,  (_book["copies"] - 1, incoming_book))
            rows_updated = cur.rowcount
            conn.commit()
            cur.close()
            print(f'rows updated {rows_updated}')
            self.books = self.__load_books()
        return _book