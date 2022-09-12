'''
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

'''


def prostie_chisla(a):
    p = []
    i = 2
    while a > 1:
        if a % 2 == 0:
            p.append(2)
            a //= 2
        else:
            i += 1
            if a % i == 0:
                p.append(i)
                a //= i
    return p


print(prostie_chisla(12))
