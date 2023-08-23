# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


N = int(input('Введите число N: '))
degree = 0
num = 1
while num < N+1:
    print(num)
    degree += 1
    num = 2 ** degree
