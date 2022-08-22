def my_func(x, y):
    if x % 2 == 0 or (x + 1) % 2 == 0:
        print("Значение x должно быть действительным положительным, значение y должно быть целым отрицательным")
    elif x > 0 > y and (y % 2 == 0 or (y + 1) % 2 == 0):
        counter = abs(y)
        res = 1
        while counter > 0:
            res = res * x
            counter = counter - 1
        return res
    else:
        print("Значение x должно быть действительным положительным, значение y должно быть целым отрицательным")


print(my_func(2.2, -3))