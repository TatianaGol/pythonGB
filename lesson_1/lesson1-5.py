'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
'''

x1 = int(input("Введите значение X для первой точки: "))
y1 = int(input("Введите значение Y для первой точки: "))
x2 = int(input("Введите значение X для второй точки: "))
y2 = int(input("Введите значение Y для второй точки: "))
ab = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
ab1 = round(ab ** 0.5, 2)
print(f"Расстояние между двумя точками - {ab1}")