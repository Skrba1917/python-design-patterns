class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):
        return f"Author {self.name} who was born in {self.birth_year}"


class Book:
    def __init__(self, title, publication_year, author: Author):
        self.title = title
        self.publication_year = publication_year
        self.author = author

    def get_book_info(self):
        return f"Book {self.title} was published in {self.publication_year} by {self.author.get_author_info()}"


author = Author("Steven", 1988)
book = Book("SkyHigh", 2015, author)

print(book.get_book_info())
