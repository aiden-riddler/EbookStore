class EBookCatalog:
    """ class for EBookCatalog """
    def __init__(self):
        self.ebooks = []

    # add ebook to catalog
    def add_ebook(self, ebook):
        self.ebooks.append(ebook)

    # remove ebook from catalog
    def remove_ebook(self, title):
        self.ebooks = [ebook for ebook in self.ebooks if ebook._title != title]

    # print ebooks in catalog
    def list_ebooks(self):
        for ebook in self.ebooks:
            print(ebook)

    # find an ebook on catalog with title
    def find_ebook(self, title):
        for ebook in self.ebooks:
            if ebook._title == title:
                return ebook
        return None
