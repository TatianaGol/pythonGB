'''
3 Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.

'''

from collections import Counter


def uniq_elem(*args):
    c = Counter(args)
    for k, v in c.items():
        if v == 1:
            print(k)


print(uniq_elem(1, 4, 5, 6, 7, 5, 3, 1, 4))
