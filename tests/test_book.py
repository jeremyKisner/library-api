from main.book import Book
import unittest

class TestBook(unittest.TestCase):

    def test_set_variables_with_none(self):
        with self.assertRaises(Exception):
            Book(None)
