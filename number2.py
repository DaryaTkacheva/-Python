a = int(input("Введите количество элементов списка "))
b = []
i = 0
el = 0
while i < a:
    b.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(b)/2)):
        b[el], b[el + 1] = b[el + 1], b[el]
        el += 2
print(b)

