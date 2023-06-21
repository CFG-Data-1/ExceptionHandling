

def add_vat(vat, prices):
    """
    Add commission to every price item in the provided iterable.

    :param vat: float, vat percentage
    :param prices: iterable, net prices as per customers' receipt
    :return: list of prices with added vat
    """
    new_prices = [(price / 100 * vat) + price for price in prices]

    return new_prices

def apply_discount(product, discount):
    """
    Add a discount to the price.
    :param product: dict obj, item spec including price
    :param discount: float discount expressed in percent
    :return: float new price
    """
    price = round(product['price'] * (1.0 - (discount / 100)), 2)
    print (price)
    assert 0 <= price <= product['price']
    return price



trainers = {'name': 'Running Trainers', 'price': 79.99}
discount = 200

print(apply_discount(trainers, discount))