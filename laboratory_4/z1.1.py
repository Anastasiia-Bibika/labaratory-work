# Завдання 1 варіант 1
# Трикутник задається координатами своїх вершин на площині.(A(x1,y1),B(x2,y2),C(x3,y3)
# Скласти програму для знаходження площі трикутника за формулою Герона.
from math import sqrt

x1 = float(input('Перша координата А: '))
y1 = float(input('Друга координата А: '))
x2 = float(input('Перша координата B: '))
y2 = float(input('Друга координата B: '))
x3 = float(input('Перша координата С: '))
y3 = float(input('Друга координата С: '))
AB = (sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))
BC = (sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2)))
AC = (sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))
p = (AB + BC + AC) / 2
S = (sqrt(p*(p-AB)*(p-BC)*(p-AC)))
print('Площа дорівнює: {0:.1f}'.format(S))