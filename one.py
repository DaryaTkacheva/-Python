a = input('Напиши свое имя: ')
b = input('Напиши имя друга/подруги: ')
c = int(input('Введи свой возраст: '))
d = int(input('Введи возраст друга/подруги: '))

if c > d:
    f = c - d
    print(a, "старше, чем", b, 'на', f, "лет/года")

elif d > c:
    f = d - c
    print(b, "старше, чем", a, 'на', f, "лет/года")
else:
    print(a, 'и', b, '- одногодки. Им', c)
