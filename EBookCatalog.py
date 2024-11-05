class EBookCatalog:
    """Class representing a catalog of eBooks."""

    def __init__(self):
        """Initialize the eBook catalog."""
        self.ebooks = []

    # Getter and Setter for eBook catalog
    def get_ebooks(self):
        """Get the list of eBooks in the catalog."""
        return self.ebooks

    def set_ebooks(self, ebooks):
        """Set the list of eBooks in the catalog."""
        self.ebooks = ebooks

    def add_ebook(self, ebook):
        """Add an eBook to the catalog."""
        self.ebooks.append(ebook)

    def remove_ebook(self, title):
        """Remove an eBook from the catalog by its title."""
        self.ebooks = [ebook for ebook in self.ebooks if ebook.get_title() != title]

    def list_ebooks(self):
        """Print the list of eBooks in the catalog."""
        for ebook in self.ebooks:
            print(ebook)

    def find_ebook(self, title):
        """Find an eBook in the catalog by its title."""
        for ebook in self.ebooks:
            if ebook.get_title() == title:
                return ebook
        return None