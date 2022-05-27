# Задача 2. Цилиндр
from math import pi as pi


def cylinder(radius, height):
    side = 2 * pi * radius * height
    full = side + 2 * side

    return side, full


r = int(input('Введите радиус цилиндра: '))
h = int(input('Введите высоту цилиндра: '))

result = cylinder(r, h)

print('Площадь боковой поверхности =', result[0])

print('Полная площадь =', result[1])

