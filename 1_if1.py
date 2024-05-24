age = int(input("Введите плиз свой возраст:"))

def your_duty():
    if age <= 4:
        duty = "Детский сад"
    elif age > 4 and age <= 18:
        duty = "Школа"
    elif age > 18 and age <= 23:
        duty = "ВУЗ"
    else:
        duty = "Работа"
    
    print(duty)

your_duty()
