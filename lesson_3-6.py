def int_func(a):
    if a.islower():
        return a.title()
    else:
        return a


print(int_func('summer'))


def title_func(a):
    line = ''
    k = a.split(' ')
    for k1 in k:
        line += f"{int_func(k1)} "
    return line


print(title_func("do homework"))