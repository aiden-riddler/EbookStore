from datetime import datetime

class Order:
    """Class representing a customer's order."""

    def __init__(self, customer, cart):
        """Initialize an order with the customer and their shopping cart."""
        self.order_date = datetime.now()
        self.order_items = cart.items.copy()
        self.total_price = cart.get_cart_total()
        self.customer = customer
        self.discount = self.calculate_discount()

    # Getters and Setters for Order attributes
    def get_order_date(self):
        """Get the order date."""
        return self.order_date

    def set_order_date(self, order_date):
        """Set the order date."""
        self.order_date = order_date

    def get_order_items(self):
        """Get the items in the order."""
        return self.order_items

    def set_order_items(self, order_items):
        """Set the items in the order."""
        self.order_items = order_items

    def get_total_price(self):
        """Get the total price of the order."""
        return self.total_price

    def set_total_price(self, total_price):
        """Set the total price of the order."""
        self.total_price = total_price

    def get_customer(self):
        """Get the customer for the order."""
        return self.customer

    def set_customer(self, customer):
        """Set the customer for the order."""
        self.customer = customer

    def get_discount(self):
        """Get the discount for the order."""
        return self.discount

    def set_discount(self, discount):
        """Set the discount for the order."""
        self.discount = discount

    def calculate_discount(self):
        """Calculate the discount for the order based on customer loyalty and bulk items."""
        discount = 0
        if self.customer.is_loyalty_member():
            discount += 0.10 * self.total_price  # 10% for loyalty members
        if len(self.order_items) >= 5:
            discount += 0.20 * self.total_price  # 20% for bulk orders
        return discount

    def get_final_total(self):
        """Calculate the final total price after applying the discount."""
        return self.total_price - self.discount

    def __str__(self):
        """Return order details as a string."""
        items = "\n".join([f"{ebook} x {qty}" for ebook, qty in self.order_items.items()])
        return f"Order Date: {self.order_date}\nItems:\n{items}\nDiscount: ${self.discount}\nTotal: ${self.get_final_total()}"
