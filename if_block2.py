balance = 1000
price = 500
in_stock = 10

print(bool(balance > price))
print(bool(in_stock))

if balance > price and in_stock:
    print('Одобряем оплату покупки')
else:
    print('Пожалуйста, пополните баланс!')