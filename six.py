a = int(input("Расстояние на первый день: "))
b = int(input("Необходимое расстояние: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
