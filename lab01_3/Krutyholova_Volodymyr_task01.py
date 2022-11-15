class Book:
    def __init__(
        self,
        author: str,
        bookName: str,
        publisher: str,
        publishYear: int,
        pagesCount: int,
    ):
        self.author = author
        self.bookName = bookName
        self.publisher = publisher
        self.publishYear = publishYear
        self.pagesCount = pagesCount

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Author has to be a string")

    @property
    def bookName(self):
        return self._bookName

    @bookName.setter
    def bookName(self, value):
        if isinstance(value, str):
            self._bookName = value
        else:
            raise ValueError("Book name has to be a string")

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        if isinstance(value, str):
            self._publisher = value
        else:
            raise ValueError("Publisher has to be a string")

    @property
    def publishYear(self):
        return self._publishYear

    @publishYear.setter
    def publishYear(self, value):
        if isinstance(value, int) and value > 0:
            self._publishYear = value
        else:
            raise ValueError("Publish year has to be a positive int")

    @property
    def pagesCount(self):
        return self._pagesCount

    @pagesCount.setter
    def pagesCount(self, value):
        if isinstance(value, int) and value > 0:
            self._pagesCount = value
        else:
            raise ValueError("Pages count has to be a positive int")


class Library:
    def __init__(self, books: list):
        self.books = books

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, array):
        for book in array:
            if not isinstance(book, Book):
                raise TypeError("Every book in list has to be of type Book")
        self._books = array

    def get_recent_books(self, authorName: str):
        result = []
        for book in self.books:
            if book.author == authorName and book.publishYear >= 2010:
                result.append(book)
        return result

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Book has to be of type Book")
        self._books.append(book)

    def remove_book(self, bookName: str):
        tempList = []
        if not isinstance(bookName, str):
            raise TypeError("Book name has to be of type string")
        for book in self.books:
            if book.bookName != bookName:
                tempList.append(book)
        self.books = tempList
