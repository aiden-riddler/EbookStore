from datetime import datetime

class Invoice:
    """Class representing an invoice for an order."""

    VAT_RATE = 0.08

    def __init__(self, order):
        """Initialize an invoice with the associated order."""
        self.order_details = order
        self.invoice_date = datetime.now()
        self.total_with_vat = self.calculate_total_with_vat()

    # Getter and Setter for order details
    def get_order_details(self):
        """Get the details of the order."""
        return self.order_details

    def set_order_details(self, order):
        """Set the order details for the invoice."""
        self.order_details = order

    def calculate_total_with_vat(self):
        """Calculate the total price with VAT."""
        total = self.order_details.get_final_total()
        return total + (total * self.VAT_RATE)

    def __str__(self):
        """Return invoice details as a string."""
        return f"Invoice Date: {self.invoice_date}\n{self.order_details}\nTotal with VAT: ${self.total_with_vat:.2f}"

