class ShoppingCart:
    # initializing the products list where the selected
    # products will be added
    def __init__(self, shop):
        self.products = {}
        self.shop = shop
    # adding the selected products to the products list
    def add_product(self, product):
        price = self.shop.get_price(product)
        self.products[product] = price