from math import sqrt
# Завдання 3.
# Трикутник задається координатами своїх вершин на площині:A(x1;y1),B(x2;y2),C(x3;y3).
#  Визначити, чи є цей трикутник виродженим
x1 = float(input('Перша координата А: '))
y1 = float(input('Друга координата А: '))
x2 = float(input('Перша координата B: '))
y2 = float(input('Друга координата B: '))
x3 = float(input('Перша координата С: '))
y3 = float(input('Друга координата С: '))

AB = (sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
BC = (sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))
AC = (sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2)))
p = (AB + BC + AC) / 2
if AC == p or BC == p or AB == p:
    print('Трикутник э виродженим')
else:
    print('Трикутник не э виродженим')