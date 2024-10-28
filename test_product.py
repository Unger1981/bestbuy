import pytest
from products import Product

def test_empty_name():
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price = 1450, quantity = 100)

def test_negative_price():
    with pytest.raises(ValueError, match="Price must be positive"):
        Product("MacBook Air M2", price = -10, quantity = 100)

def test_zero_quantity():
    product = Product("TestProduct", 999, 1)
    product.set_quantity(1)

    assert product.active == False        


def test_purchase_quantity():
    product = Product("TestProduct",100,10)
    product.buy(5)

    assert product.quantity == 5

def test_insufficient_quantity():
    with pytest.raises(ValueError, match="Stock quantity not sufficient"):

        product = Product("TestProduct",100,10)
        product.buy(15)


