""" Реализуйте алгоритм перемешивания списка. """
import random

size = int(input('Enter list size: '))
lst = []
for i in range(size):
    lst.append(i)
print(lst)

count = 0
while count < len(lst) * 100:
    a = random.randrange(0, len(lst))
    b = random.randrange(0, len(lst))
    if a != b:
        lst[a], lst[b] = lst[b], lst[a]
        count += 1
    else:
        continue
print(lst)





