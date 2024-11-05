class ShoppingCart:
    """Class representing a shopping cart containing eBooks."""

    def __init__(self):
        """Initialize the shopping cart with an empty list of items."""
        self.items = {}

    # Getter and Setter for shopping cart items
    def get_items(self):
        """Get the items in the shopping cart."""
        return self.items

    def set_items(self, items):
        """Set the items in the shopping cart."""
        self.items = items

    def add_to_cart(self, ebook, quantity=1):
        """Add an eBook to the shopping cart."""
        if ebook in self.items:
            self.items[ebook] += quantity
        else:
            self.items[ebook] = quantity

    def remove_from_cart(self, ebook):
        """Remove an eBook from the shopping cart."""
        if ebook in self.items:
            del self.items[ebook]

    def get_cart_total(self):
        """Calculate the total price of items in the shopping cart."""
        return sum(ebook.get_price() * qty for ebook, qty in self.items.items())

    def list_cart_items(self):
        """Print the items in the shopping cart."""
        for ebook, qty in self.items.items():
            print(f"{ebook} x {qty}")

    def clear_cart(self):
        """Remove all items from the shopping cart."""
        self.items = {}