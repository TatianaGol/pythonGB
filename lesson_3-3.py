def my_func(a, b, c):
    if a > b >= c or b > a >= c:
        return a + b
    elif b > c >= a or c > b >= a:
        return b + c
    elif c > a >= b or a > c >= b:
        return c + a
    else:
        return a


print(my_func(1, 1, 10))