'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def fib(k):
    list_k = [1, -1]
    list_k_positive = [0, 1]
    i = 0
    l = 0
    while i <= k - 3:
        list_k.append(list_k[i] - list_k[i + 1])
        i += 1
    list_k.reverse()
    while l <= k - 2:
        list_k_positive.append(list_k_positive[l] + list_k_positive[l + 1])
        l += 1
    list_k.extend(list_k_positive)
    return list_k


print(fib(8))
