'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


def pairs(*args):
    k = []
    list_args = list(args)
    f = 0
    l = -1
    if len(list_args) % 2 == 1:
        while f < len(list_args) // 2 and l > -len(list_args) // 2:
            k.append(list_args[f] * list_args[l])
            f += 1
            l -= 1
        k.append(list_args[len(list_args) // 2] ** 2)
        return k
    elif len(list_args) % 2 == 0:
        while f < len(list_args) // 2 and l > -len(list_args) - 1 // 2:
            k.append(list_args[f] * list_args[l])
            f += 1
            l -= 1
        return k


print(pairs(1, 6, 5, 15, 8))


