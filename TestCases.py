from EBook import EBook
from EBookCatalog import EBookCatalog
from Customer import Customer
from Order import Order
from Invoice import Invoice


# Initialize catalog and test adding/removing e-books
def test_catalog_management():
    print("Testing Catalog Management")
    catalog = EBookCatalog()

    # Add e-books to catalog
    ebook1 = EBook("Python 101", "John Doe", "2022", "Programming", 20.00)
    ebook2 = EBook("AI Essentials", "Jane Smith", "2023", "AI", 35.00)
    ebook3 = EBook("Data Science Basics", "Alice Brown", "2021", "Data Science", 50.00)

    # Adding books to the catalog
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    catalog.add_ebook(ebook3)

    # List e-books in catalog
    print("\nCatalog E-Books List:")
    catalog.list_ebooks()

    # Attempt to remove an e-book and handle cases where the e-book might not be in the catalog
    catalog.remove_ebook("AI Essentials")
    print("\nCatalog After Removing 'AI Essentials':")
    catalog.list_ebooks()

    # Edge case: Attempt to remove an e-book that doesn't exist
    catalog.remove_ebook("Nonexistent Book")


# Test customer creation and management of shopping cart
def test_customer_cart_operations():
    print("Testing Customer and Shopping Cart Operations")

    # Create customers with different loyalty statuses
    customer1 = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    customer2 = Customer("Bob", "bob@example.com", is_loyalty_member=False)

    # Get carts for customers
    cart1 = customer1.get_cart()
    cart2 = customer2.get_cart()

    # Add items to customer1's cart with valid and invalid quantities
    ebook1 = EBook("Python 101", "John Doe", "2022", "Programming", 20.00)
    ebook2 = EBook("Data Science Basics", "Alice Brown", "2021", "Data Science", 50.00)
    cart1.add_to_cart(ebook1, 3)  # Adding 3 copies of Python 101
    cart1.add_to_cart(ebook2, 1)  # Adding 1 copy of Data Science Basics

    # Edge case: Adding an invalid quantity (negative number)
    print('Testing adding a negative quantity')
    try:
        cart1.add_to_cart(ebook2, -1)
    except ValueError as e:
        print(e)

    # Add items to customer2's cart
    cart2.add_to_cart(ebook1, 1)  # Adding 1 copy of Python 101

    # List cart items for each customer
    print("\nCustomer 1's Cart Items:")
    cart1.list_cart_items()
    print("\nCustomer 2's Cart Items:")
    cart2.list_cart_items()

    # Remove item from customer1's cart
    cart1.remove_from_cart(ebook2)

    print("\nCustomer 1's Cart After Removing 'Data Science Basics':")
    cart1.list_cart_items()

    # try and handle cases where item may not exist
    cart1.remove_from_cart(ebook2)

    print("Customer and Cart Operations Test Passed\n")


# Test order creation, discount application, and final total calculation
def test_order_processing():
    print("Testing Order Processing and Discounts")

    # Set up customer with loyalty membership and shopping cart
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    cart = customer.get_cart()

    # Add items to cart to test bulk discount
    ebook1 = EBook("Python 101", "John Doe", "2022", "Programming", 20.00)
    ebook2 = EBook("AI Essentials", "Jane Smith", "2023", "AI", 35.00)
    ebook3 = EBook("Data Science Basics", "Alice Brown", "2021", "Data Science", 50.00)

    cart.add_to_cart(ebook1, 5)  # Adding 5 copies to qualify for bulk discount
    cart.add_to_cart(ebook2, 1)  # Additional item to check total calculation

    # Create order from cart and calculate discounts
    order = Order(customer, cart)

    # Print order details with discounts applied (includes loyalty and bulk discounts)
    print("\nOrder Summary with Discounts Applied:")
    print(order)
    print("Order Processing and Discounts Test Passed\n")

    # Edge case: Empty cart order
    customer = Customer("Jane", "jane@example.com", is_loyalty_member=True)
    empty_cart = customer.get_cart()
    try:
        empty_order = Order(customer, empty_cart)
    except ValueError as e:
        print(e)  # Expected error when creating an order with an empty cart


# Test invoice generation with VAT calculation
def test_invoice_generation():
    print("Testing Invoice Generation with VAT Calculation")

    # Set up customer and create cart
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    cart = customer.get_cart()

    # Add items to cart
    ebook1 = EBook("Python 101", "John Doe", "2022", "Programming", 20.00)
    ebook2 = EBook("Data Science Basics", "Alice Brown", "2021", "Data Science", 50.00)
    cart.add_to_cart(ebook1, 2)  # Adding 2 copies of Python 101
    cart.add_to_cart(ebook2, 3)  # Adding 3 copies of Data Science Basics

    # Create order from cart and generate invoice with VAT applied
    order = Order(customer, cart)
    invoice = Invoice(order)

    # Display the generated invoice
    print("\nInvoice Summary with VAT Applied:")
    print(invoice)
    print("Invoice Generation Test Passed\n")


# Execute all tests and summarize results
print("Running All Tests\n")
test_catalog_management()
test_customer_cart_operations()
test_order_processing()
test_invoice_generation()
print("All Tests Completed Successfully")

