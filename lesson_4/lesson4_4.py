'''
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

*Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import itertools
import random


def stroka(k):
    int_list = [random.randrange(1, 100) for i in range(k + 1)]
    stroka1 = ['*x^'] * (k - 1) + ['*x']
    p = [[a, b, c] for a, b, c in zip(int_list, stroka1, range(k, 1, -1)) if a != 0]
    for x in p:
        x.append(' + ')
    p = list(itertools.chain(*p))
    p[-1] = ' = 0'
    return ''.join(map(str, p)).replace(' 1*x', ' x')


print(stroka(4))

with open('func.txt', 'w') as data:
    data.write(stroka(4))
with open('func2.txt', 'w') as data:
    data.write(stroka(4))

