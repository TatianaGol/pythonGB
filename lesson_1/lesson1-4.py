'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
'''

x = int(input("Введите номер четверти плоскости: "))
if x == 1:
    print("Диапозон чисел x - от 0 до бесконечности, y - от 0 до бесконечности")
elif x == 2:
    print("Диапозон чисел x - от -бесконечности до 0, y - от 0 до бесконечности")
elif x == 3:
    print("Диапозон чисел x - от -бесконечности до 0, y - от -бесконечности до 0")
elif x == 4:
    print("Диапозон чисел x - от 0 до бесконечности, y - от -бесконечности до 0")
else:
    print("Такой четверти плоскости не существует")