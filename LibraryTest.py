import unittest
from Library import Library, Patron, Book, Album, Movie


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.patron = Patron("p1", "Alice")
        self.book = Book("b1", "1984", "George Orwell")
        self.album = Album("a1", "Thriller", "Michael Jackson")
        self.movie = Movie("m1", "Inception", "Christopher Nolan")

        self.library.add_patron(self.patron)
        self.library.add_library_item(self.book)
        self.library.add_library_item(self.album)
        self.library.add_library_item(self.movie)

    def test_checkout_book(self):
        result = self.library.check_out_library_item("p1", "b1")
        self.assertEqual(result, "check out successful")
        self.assertEqual(self.book.get_location(), "CHECKED_OUT")
        self.assertEqual(self.book.get_checked_out_by(), self.patron)
        self.assertIn(self.book, self.patron.get_checked_out_items())

    def test_return_book(self):
        self.library.check_out_library_item("p1", "b1")
        result = self.library.return_library_item("b1")
        self.assertEqual(result, "return successful")
        self.assertEqual(self.book.get_location(), "ON_SHELF")
        self.assertIsNone(self.book.get_checked_out_by())
        self.assertNotIn(self.book, self.patron.get_checked_out_items())

    def test_fine_increment(self):
        self.library.check_out_library_item("p1", "b1")
        self.library._current_date = 22
        self.library.increment_current_date() 
        self.assertGreater(self.patron.get_fine_amount(), 0)

if __name__ == '__main__':
    unittest.main()
