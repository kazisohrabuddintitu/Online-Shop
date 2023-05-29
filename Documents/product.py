class Product:
    # Initializing
    def __init__(self, name, price, shop):
        self.name = name
        self.price = price
        self.shop = shop
        self.shop.addProduct(self.name, self.price)
    
    def display_product(self):
        print('Product:', self.name, self.price)