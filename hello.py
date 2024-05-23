from pprint import pprint

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 124234.1,
        'recommended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000}
]

stock[0]["recommended"].append("Xiaomi Mi11")
stock[2]["price"] = stock[2]["price"] - 30000
pprint(stock)