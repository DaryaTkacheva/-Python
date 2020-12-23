
a=123
b=1.23
c="Абвгд"
d=['а', 'б', 'в']
e=('а', '1')
f=(2+3j)
g={'word_1': 'one', 'word_2': 'two'}

list=[a, b, c, d, e, f, g]
for i in list:
    print(f'{i} is {type(i)}')

