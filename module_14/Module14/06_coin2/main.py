import math

print('введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('введите радиус: '))

xy = math.sqrt(x ** 2 + y ** 2)

if xy <= radius:
    print('\nмонетка где-то рядом')
else:
    print('\nмонетки в области нет')
