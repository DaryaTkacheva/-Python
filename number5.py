n = int(input("Введите число: "))
a = [7, 4, 3, 2]
c = a.count(n)
for i in a:
    if c > 0:
        j = a.index(n)
        a.insert(i+c, n)
        break
    else:
        if n > i:
            l = a.index(i)
            a.insert(l, n)
            break
        elif n < a[len(a) - 1]:
            a.append(n)
print(a)