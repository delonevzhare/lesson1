import random

x = random.randint(0, 10)

def more_or_less(num):
    if x > 5: 
        print('Больше')
    else:
        print('Меньше')

more_or_less(x)

x = 0

while x < 10:
    print(x)
    x = x +1
