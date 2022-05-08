def division_numbers():
    try:
        number1 = int(input("Введите число №1 "))
        number2 = int(input("Введите число №2 "))
        return number1 / number2
    except ZeroDivisionError:
        print("Division by zero is prohibited")


print(division_numbers())