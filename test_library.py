from library import Library, Book
import pytest


@pytest.fixture
def lib_empty() -> Library:
    return Library()


book_list = [
    Book("Shakespear", "McBeth"),
    Book("Shakespear", "Romeo and Juliet"),
    Book("Katzenbach", "Blue"),
]


@pytest.fixture
def lib_populated(lib_empty: Library) -> Library:
    for book in book_list:
        lib_empty.add_book(title=book.title, author=book.author)
    return lib_empty


def test_add_book(lib_empty: Library):
    book_to_add = book_list[0]
    lib_empty.add_book(book_to_add.title, book_to_add.author)
    assert book_list[0] in lib_empty.books


def test_delete_book(lib_populated: Library):
    book_to_delete = book_list[1]
    lib_populated.delete_book(book_to_delete)

    assert book_to_delete not in lib_populated.books


def test_list_books(lib_populated: Library):
    assert set(lib_populated.books) == set(book for book in book_list)


def test_search_book_author(lib_populated: Library):
    author = "Shakespear"
    assert set(lib_populated.search_book_author(author)) == set(
        book for book in book_list if book.author == author
    )


def test_gen_stats(lib_populated: Library):
    book_cnt_expected = 0
    authors_expected = set()
    for book in book_list:
        book_cnt_expected += 1
        authors_expected.add(book.author)

    book_cnt_actual, authors_actual = lib_populated.generate_stats()
    assert book_cnt_actual == book_cnt_expected
    assert authors_actual == authors_actual
