age = int(input("Введите плиз свой возраст:"))

def your_duty(age):
    if 4 < age <= 18:
        duty = "Школа"
    elif 18 < age <= 23:
        duty = "ВУЗ"
    elif age <= 4:
        duty = "Детский сад"
    else:
        duty = "Работа"
    
    print(duty)

your_duty(age)
