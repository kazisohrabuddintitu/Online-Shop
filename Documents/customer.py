from shopping_cart import ShoppingCart
class Customer:
    # Initializing the customer class
    def __init__(self, name, id, shop):
        self.name = name
        self.id = id
        self.shop = shop
        self.sum = 0.0
        self.shoppingcart = ShoppingCart(self.shop) # Instantiate a ShoppingCard object
    
    # Adding the product to the shopping cart
    def add_product(self, product):
        self.shoppingcart.add_product(product)
    
    def display_cart(self):
        total = 0
        print("{} your cart is: ".format(self.name))
        for product, price in self.shoppingcart.products.items():
            print(f"{product}: {price}")
            total = self.add_total(price)
        print("Total is: {} TK".format(total))
    
    # Returning the price 
    def add_total(self, price):
        self.sum =self.sum + price
        return self.sum

    
    