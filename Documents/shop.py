class Shop:
    def __init__(self):
        self.product_list = {}
         
    def addProduct(self, product, price):
        self.product_list[product] = price

    def display_product(self):
        print('Available Products are:')
        for product, price in self.product_list.items():
            print(f"{product}: {price}")
    
    def get_price(self, product):
        return self.product_list.get(product)