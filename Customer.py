from ShoppingCart import ShoppingCart


class Customer:
    """ class for customer """
    def __init__(self, name, contact_info, is_loyalty_member=False):
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member
        self._shopping_cart = ShoppingCart()

    # get customer's shopping cart
    def get_cart(self):
        return self._shopping_cart

    # check customer's loyalty
    def is_loyalty_member(self):
        return self._is_loyalty_member

    # get customer details
    def __str__(self):
        return f"Customer: {self._name}, Contact: {self._contact_info}, Loyalty Member: {self._is_loyalty_member}"
