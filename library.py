from dataclasses import dataclass
from typing import Generator, List


@dataclass
class Book:
    author: str
    title: str

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.author == other.author and self.title == other.title

    def __hash__(self):
        # Use hash() on a tuple of the attributes to generate a hash value
        return hash((self.author, self.title))


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str) -> None:
        self.books.append(Book(author=author, title=title))

    def delete_book(self, book_to_delete: Book):
        """What aabout multiple same books? What about same title from different author?"""
        self.books = [book for book in self.books if book.title != book_to_delete.title]

    def list_books(self) -> List[Book]:
        return list(set(book for book in self.books))

    def search_book_author(self, author: str) -> Generator:
        return (book for book in self.books if book.author == author)

    def generate_stats(self):
        book_cnt = 0
        authors = set()
        for book in self.books:
            book_cnt += 1
            authors.add(book.author)

        return book_cnt, authors
