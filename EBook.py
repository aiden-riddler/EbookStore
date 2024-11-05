class EBook:
    """ class for Ebook """

    def __init__(self, title, author, publication_date, genre, price):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # get price of Ebook
    def get_price(self):
        return self._price

    # get Ebook details
    def __str__(self):
        return f"{self._title} by {self._author} - {self._genre} - ${self._price}"
