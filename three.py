n = int(input('Введите число от 0 до 9: '))
if n < 10:
    n = n + 11*n + 111*n
    print(n)
else:
    print('Error')
