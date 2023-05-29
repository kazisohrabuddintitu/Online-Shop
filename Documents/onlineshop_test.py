# from ..Documents.product import Product
from ..Documents.product import Product

def test_product():
    product = Product("A", 100)
    
    assert product.name == 'A'
    assert product.price == 100
    
test_product()