class EBook:
    """Class representing an eBook with title, author, publication date, genre, and price."""

    def __init__(self, title, author, publication_date, genre, price):
        """Initialize an eBook with title, author, publication date, genre, and price."""
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # Getters and Setters for EBook attributes
    def get_title(self):
        """Get the eBook's title."""
        return self._title

    def set_title(self, title):
        """Set the eBook's title."""
        self._title = title

    def get_author(self):
        """Get the eBook's author."""
        return self._author

    def set_author(self, author):
        """Set the eBook's author."""
        self._author = author

    def get_publication_date(self):
        """Get the eBook's publication date."""
        return self._publication_date

    def set_publication_date(self, publication_date):
        """Set the eBook's publication date."""
        self._publication_date = publication_date

    def get_genre(self):
        """Get the eBook's genre."""
        return self._genre

    def set_genre(self, genre):
        """Set the eBook's genre."""
        self._genre = genre

    def get_price(self):
        """Get the eBook's price."""
        return self._price

    def set_price(self, price):
        """Set the eBook's price."""
        self._price = price

    def __str__(self):
        """Return eBook details as a string."""
        return f"{self._title} by {self._author} - {self._genre} - ${self._price}"