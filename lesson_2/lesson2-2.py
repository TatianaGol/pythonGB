'''
 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

n = int(input("Введите число: "))
b = [1]
k = 2
while (n > 1):
    b.append(b[-1] * k)
    k += 1
    n -= 1

print(b)