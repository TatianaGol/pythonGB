'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


def sumfloat(*args):
    k = []
    for i in args:
        k.append(abs(round(i % 1, 3)))
    max_k = k[0]
    min_k = k[0]
    for i in k:
        if i > max_k:
            max_k = i
    for i in k:
        if i < min_k:
            min_k = i
    return round(max_k - min_k, 3)


print(sumfloat(1.63, 4.85, 9.86, 0.9))
