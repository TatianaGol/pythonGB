def numbers_sum():
    k = 0
    while True:
        try:
            inp = map(int, input("Введите числа через пробел: ").split(' '))
            k += sum(inp)
            print(k)
            if inp == '&':
                break
                print(k)
        except ValueError:
            return k


print(numbers_sum())