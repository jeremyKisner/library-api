from main.book import Book
import unittest

class TestBook(unittest.TestCase):

    def setUp(self) -> None:
        test_book_info = {
            "name": "test",
            "author": "Author Name",
            "type": "FICTION",
            "isbn_13": "1234",
            "isbn_10": "1",
            "published": "2023",
            "publisher": "Test Publisher",
            "copies": "2",
        }
        self.book = Book(test_book_info)


    def test_set_variables_with_none(self):
        with self.assertRaises(ValueError) as cm:
            Book(None)
        self.assertEqual(str(cm.exception), "Expected record for book!")


    def test_set_variables_with_empty(self):
        with self.assertRaises(ValueError) as cm:
            Book({})
        self.assertEqual(str(cm.exception), "Expected record for book!")
        with self.assertRaises(ValueError) as cm:
            Book([])
        self.assertEqual(str(cm.exception), "Expected record for book!")


    def test_get(self):
        self.assertIsNotNone(self.book)
        self.assertIsNotNone(self.book.get())
        self.assertEqual(self.book.get()[0], "test")
        self.assertEqual(self.book.get()[1], "Author Name")
        self.assertEqual(self.book.get()[2], "FICTION")
        self.assertEqual(self.book.get()[3], 1234)
        self.assertEqual(self.book.get()[4], 1)
        self.assertEqual(self.book.get()[5], "2023")
        self.assertEqual(self.book.get()[6], "Test Publisher")
        self.assertEqual(self.book.get()[7], 2)


    def test_with_name(self):
        self.assertEqual(self.book.get_name(), "test")


    def test_with_author(self):
        self.assertEqual(self.book.get_author(), "Author Name")


    def test_with_type(self):
        self.assertEqual(self.book.get_type(), "FICTION")


    def test_with_isbn_13(self):
        self.assertEqual(self.book.get_isbn_13(), 1234)


    def test_with_isbn_10(self):
        self.assertEqual(self.book.get_isbn_10(), 1)


    def test_with_published(self):
        self.assertEqual(self.book.get_published(), "2023")


    def test_with_publisher(self):
        self.assertEqual(self.book.get_publisher(), "Test Publisher")


    def test_with_copies(self):
        self.assertEqual(self.book.get_copies(), 2)
