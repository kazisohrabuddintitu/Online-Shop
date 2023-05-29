from customer import Customer
from product import Product
from shop import Shop

# Creating instances of the classes
shop = Shop()

Product("t-shirt", 1000.0, shop)
Product("Jeans", 2000.0, shop)


customer = Customer("Kazi Sohrab", 12345, shop)

# Calling methods of the classes
customer.add_product("t-shirt")
customer.add_product("Jeans")

customer.display_cart()# Products added cart