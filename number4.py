a = input("введите строку ")
b = []
c = 1
for i in range(a.count(' ') + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {c} {b [i]}")
        c += 1
    else:
        print(f" {c} {b [i] [0:10]}")
        c += 1