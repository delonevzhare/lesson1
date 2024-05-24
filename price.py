def discounter(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

product = {'name': 'Samsung Galaxy S21', 'price': 50000, 'discount': 5}
product['with_discount'] = discounter(product['price'], product['discount'])
print(product)