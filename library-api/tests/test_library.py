import unittest
import main.library as t

class TestLibrary(unittest.TestCase):


    def test_library(self):
        library = t.Library()
        self.assertIsNotNone(library)
        self.assertIsNotNone(library.inventory)


    def test_library_load_inventory(self):
        library = t.Library()
        self.assertIsNotNone(library.__load_inventory__())


    def test_get_inventory(self):
        library = t.Library()
        self.assertIsNotNone(library.get_inventory())
        for item in library.get_inventory():
            self.assertIsNotNone(item)


    def test_add_inventory_single_item(self):
        library = t.Library()
        new_book = {
            "name": "New Testable Book",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 1,
            "isbn-10": 1,
            "published": 2023,
            "publisher": "test"
        }
        original_len = len(library.inventory)
        self.assertTrue(library.add_inventory(new_book))
        self.assertEqual(original_len + 1, len(library.inventory))
        new_book = {
            "name": "New Testable Book II",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 2,
            "isbn-10": 2,
            "published": 2023,
            "publisher": "test"
        }
        self.assertTrue(library.add_inventory(new_book))
        self.assertEqual(original_len + 2, len(library.inventory))


    def test_add_inventory_multiple_items(self):
        library = t.Library()
        new_books = [
            {
            "name": "New Testable Book",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 1,
            "isbn-10": 1,
            "published": 2023,
            "publisher": "test"
        },
        {
            "name": "New Testable Book II",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 2,
            "isbn-10": 2,
            "published": 2023,
            "publisher": "test"
        }
        ]
        current_len = len(library.inventory)
        self.assertTrue(library.add_inventory(new_books))
        self.assertEqual(current_len + 2, len(library.inventory))


    def test_get_book_with_none(self):
        library = t.Library()
        result = library.get_book(None)
        self.assertEqual([], result)


    def test_get_book_with_name(self):
        library = t.Library()
        new_books = [
            {
            "name": "New Testable Book",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 1,
            "isbn-10": 1,
            "published": 2023,
            "publisher": "test"
        },
        {
            "name": "New Testable Book II",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 2,
            "isbn-10": 2,
            "published": 2023,
            "publisher": "test"
        }
        ]
        library.add_inventory(new_books)
        wanted_book = {
            "name": "new testable book"
        }
        result = library.get_book(wanted_book)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)


    def test_delete_book(self):
        library = t.Library()
        new_book = {
            "name": "New Testable Book",
            "author": "test",
            "type": "non-fiction",
            "isbn_13": 1,
            "isbn-10": 1,
            "published": 2023,
            "publisher": "test"
        }
        original_len = len(library.get_inventory())
        library.add_inventory(new_book)
        self.assertEqual(original_len + 1, len(library.get_inventory()))
        library.delete_book({"isbn_13": 1})
        self.assertEqual(original_len, len(library.get_inventory()))
