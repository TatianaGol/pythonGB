'''
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов.
'''

path = 'func.txt'
data = open(path, 'r')
str1 = data.readline()
data.close()
path2 = 'func2.txt'
data2 = open(path2, 'r')
str2 = data2.readline()
data2.close()
part_1 = str1.split('=')
part_2 = str2.split('=')
str_3 = f'{part_1[0]} + {part_2[0]} = 0'
print(str_3)
path3 = 'func3.txt'
data3 = open(path3, 'w')
data3.write(str_3)
data3.close()
