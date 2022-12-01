""" Задайте список из N элементов, заполненных числами
    из промежутка [-N, N]. Найдите произведение элементов
    на указанных позициях. Позиции хранятся в файле file.txt
    в одной строке одно число.                          """

n = int(input('Введите число n: '))
lst = []
for i in range(-n, n + 1):
    lst.append(i)
    if i == n:
        print(i)
    else:
        print(i, end=' ')

file = open('file.txt', 'r', encoding='UTF-8')
f = file.read().splitlines()
print(f'{lst[int(f[0])]} * {lst[int(f[1])]} = {lst[int(f[0])] * lst[int(f[1])]}')
file.close()


