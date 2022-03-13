

class Book():

    def __init__(self, isbn=None, title=None, author=None, publisher=None, price=None, desc=None) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.desc = desc


if __name__ == '__main__':
    a = Book()
    a.desc = 100
    print("desc: ", a.desc)
