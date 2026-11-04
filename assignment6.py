"""A small library program with books and people who borrow them."""

# Mohamed Houqe
# Python Programming - Module 6, Assignment 1


class Book:
    """Keep a book's details and track whether it is borrowed."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Change this value through the book's methods.
        self._is_borrowed = False

    @property
    def is_borrowed(self):
        """Let other code check the book's status without setting it."""
        return self._is_borrowed

    def borrow(self):
        """Borrow the book if it is available and return True."""
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        return True

    def return_book(self):
        """Return a borrowed book, or return False if it is already here."""
        if not self._is_borrowed:
            return False
        self._is_borrowed = False
        return True

    def __str__(self):
        if self._is_borrowed:
            status = "borrowed"
        else:
            status = "available"
        return f"{self.title} by {self.author} - {status}"


class EBook(Book):
    """Use the Book methods and add a file size for a digital book."""

    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        if file_size_mb <= 0:
            raise ValueError("The file size must be greater than 0.")
        self.file_size_mb = file_size_mb

    def __str__(self):
        # Add the file size to the normal book description.
        return f"{super().__str__()} | Ebook size: {self.file_size_mb} MB"


class Patron:
    """Keep track of the books a person has borrowed."""

    def __init__(self, name):
        self.name = name
        self._books = []

    def borrow_book(self, book):
        """Ask the book if it is available before adding it to the list."""
        if book.borrow():
            self._books.append(book)
            return f"{self.name} borrowed {book.title}."
        return f"{book.title} is already borrowed."

    def return_book(self, book):
        """Only return a book if this person has borrowed it."""
        if book not in self._books:
            return f"{self.name} has not borrowed {book.title}."
        book.return_book()
        self._books.remove(book)
        return f"{self.name} returned {book.title}."

    def __str__(self):
        return f"{self.name} has {len(self._books)} borrowed book(s)."


def main():
    """Show how the books and patrons work together."""
    book = Book("Campus Stories", "Sam Lee")
    ebook = EBook("Study Tips", "Mina Khan", 2.5)
    mohamed = Patron("Mohamed")
    sara = Patron("Sara")

    print("Small Library Demo")
    print(book)
    print(ebook)
    print()

    print(mohamed.borrow_book(book))
    print(sara.borrow_book(book))
    print(mohamed.borrow_book(ebook))
    print(sara.return_book(book))
    print(mohamed.return_book(book))
    print(sara.borrow_book(book))

    print()
    print(book)
    print(ebook)
    print(mohamed)
    print(sara)


if __name__ == "__main__":
    main()
