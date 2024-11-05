class ShoppingCart:
    """ class for shopping cart"""
    def __init__(self):
        self.items = {}

    # add ebook to cart
    def add_to_cart(self, ebook, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")
        if ebook in self.items:
            self.items[ebook] += quantity
        else:
            self.items[ebook] = quantity

    # remove ebook from cart
    def remove_from_cart(self, ebook):
        if ebook in self.items:
            del self.items[ebook]

    # get total price of items in cart
    def get_cart_total(self):
        return sum(ebook.get_price() * qty for ebook, qty in self.items.items())

    # print shopping cart
    def list_cart_items(self):
        for ebook, qty in self.items.items():
            print(f"{ebook} x {qty}")

    # remove all items from cart
    def clear_cart(self):
        self.items = {}
