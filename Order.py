from datetime import datetime

class Order:
    """ class for order """
    def __init__(self, customer, cart):
        if len(cart.items) == 0:
            raise ValueError('Cannot make order. Cart is empty!')
        self.order_date = datetime.now()
        self.order_items = cart.items.copy()
        self.total_price = cart.get_cart_total()
        self.customer = customer
        self.discount = self.calculate_discount()

    # calculate customer discount based on loyalty
    def calculate_discount(self):
        discount = 0
        if self.customer.is_loyalty_member():
            discount += 0.10 * self.total_price  # 10% for loyalty members
        if len(self.order_items) >= 5:
            discount += 0.20 * self.total_price  # 20% for bulk orders
        return discount

    # get final total price
    def get_final_total(self):
        return self.total_price - self.discount

    # get order details
    def __str__(self):
        items = "\n".join([f"{ebook} x {qty}" for ebook, qty in self.order_items.items()])
        return f"Order Date: {self.order_date}\nItems:\n{items}\nDiscount: ${self.discount}\nTotal: ${self.get_final_total()}"
