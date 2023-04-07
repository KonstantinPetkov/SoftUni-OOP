from unittest import TestCase,main
from project.bookstore import Bookstore

class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(15)
        self.books = {
            "Java": 10,
            "C#": 3,
        }

    def test_valid__init(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_invalid_books_limit_set_raises_error(self):
        with self.assertRaises(ValueError) as err:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(err.exception))

    def test_correct__len__method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(13, len(self.store))

    def test_not_enough_space_to_recieve_book_in_bookstore_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Python", 5)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book_correct(self):
        result = self.store.receive_book("Python", 1)
        self.assertEqual("1 copies of Python are available in the bookstore.", result)

        self.assertEqual({"Python": 1}, self.store.availability_in_store_by_book_titles)

    def test_add_existing_book_correct(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.receive_book("C#", 2)
        self.assertEqual("5 copies of C# are available in the bookstore.", result)

    def test_sell_book_that_is_not_available_in_bookstore_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Python", 1)

        self.assertEqual("Book Python doesn't exist!", str(ex.exception))

    def test_sell_more_copies_then_avalability_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("C#", 4)

        self.assertEqual("C# has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_successfully(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.sell_book("C#", 3)

        self.assertEqual({"Java": 10, "C#": 0}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual("Sold 3 copies of C#", result)

    def test_correct__str__method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(
            "Total sold books: 0\n"
            "Current availability: 13\n"
            " - Java: 10 copies\n"
            " - C#: 3 copies",
            str(self.store)
        )


if __name__ == '__main__':
    main()