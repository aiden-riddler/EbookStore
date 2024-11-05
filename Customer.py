from ShoppingCart import ShoppingCart


class Customer:
    """Class representing a customer with contact details, loyalty membership, and a shopping cart."""

    def __init__(self, name, contact_info, is_loyalty_member=False):
        """Initialize a Customer with name, contact info, and loyalty membership."""
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member
        self._shopping_cart = ShoppingCart()

    # Getter and Setter for name
    def get_name(self):
        """Get the customer's name."""
        return self._name

    def set_name(self, name):
        """Set the customer's name."""
        self._name = name

    # Getter and Setter for contact info
    def get_contact_info(self):
        """Get the customer's contact information."""
        return self._contact_info

    def set_contact_info(self, contact_info):
        """Set the customer's contact information."""
        self._contact_info = contact_info

    # Getter and Setter for loyalty membership
    def get_is_loyalty_member(self):
        """Check if the customer is a loyalty member."""
        return self._is_loyalty_member

    def set_is_loyalty_member(self, is_loyalty_member):
        """Set the customer's loyalty membership status."""
        self._is_loyalty_member = is_loyalty_member

    # Getter for shopping cart
    def get_cart(self):
        """Retrieve the customer's shopping cart."""
        return self._shopping_cart

    def __str__(self):
        """Return customer details as a string."""
        return f"Customer: {self._name}, Contact: {self._contact_info}, Loyalty Member: {self._is_loyalty_member}"
