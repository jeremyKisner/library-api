import unittest
import main.library as t

class TestLibrary(unittest.TestCase):


    def test_library(self):
        library = t.Library()
        self.assertIsNotNone(library)
        self.assertIsNotNone(library.inventory)
        self.assertIsNotNone(library.isbn_13)


    def test_library_load_inventory(self):
        library = t.Library()
        self.assertIsNotNone(library.load_inventory())


    def test_get_inventory(self):
        library = t.Library()
        self.assertIsNotNone(library.get_inventory())
        for item in library.get_inventory():
            self.assertIsNotNone(item)


    def test_add_inventory(self):
        library = t.Library()
        new_book = {
            "name": "New Testable Book",
            "author": "test",
            "type": "non-fiction",
            "isbn-13": 1,
            "isbn-10": 1,
            "published": 2023,
            "publisher": "test"
        }
        self.assertTrue(library.add_inventory(new_book))
