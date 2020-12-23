m = int(input("Введите месяц в числовом формате:" ))
vg = ["Зима", "Весна", "Лето", "Осень"]
a = { 1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень' }
if m == 1 or m == 2 or m == 12:
    print(a.get(1))
    print(vg[0])
elif m == 3 or m == 4 or m == 5:
    print(a.get(2))
    print(vg[1])
elif m == 6 or m == 7 or m == 8:
    print(a.get(3))
    print(vg[2])
elif m == 9 or m == 10 or m == 11:
    print(a.get(4))
    print(vg[3])
else:
    print('Error')





