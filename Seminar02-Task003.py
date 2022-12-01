n = int(input('Введите число n: '))
res = 0
s = 0
print('[', end='')
for i in range(1, n + 1):
    res = (1 + 1 / i) ** i
    if i == n:
        print('{:.3}'.format(res), end=']')
    else:
        print('{:.3}'.format(res), end=', ')
    s += res
print(f'\nСумма: {str(s)[:4]}')
