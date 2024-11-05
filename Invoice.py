from datetime import datetime


class Invoice:
    """ class for invoice """
    VAT_RATE = 0.08

    def __init__(self, order):
        self.order_details = order
        self.invoice_date = datetime.now()
        self.total_with_vat = self.calculate_total_with_vat()

    # get total cosst with VAT
    def calculate_total_with_vat(self):
        total = self.order_details.get_final_total()
        return total + (total * self.VAT_RATE)

    # get invoice details
    def __str__(self):
        return f"Invoice Date: {self.invoice_date}\n{self.order_details}\nTotal with VAT: ${self.total_with_vat:.2f}"
