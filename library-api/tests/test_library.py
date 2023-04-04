import unittest
import main.library as t

class TestLibrary(unittest.TestCase):


    def test_library(self):
        library = t.Library()
        self.assertIsNotNone(library)
        self.assertIsNotNone(library.inventory)
