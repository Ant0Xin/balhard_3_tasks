"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию square, которая принимает длину стороны квадрата
таким образом, чтобы она возвращала 3 значения:
    - периметр квадрата
    - площадь квадрата
    - диагональ квадрата

ПРИМЕРЫ
--------------------------------------------------------------------------------
- square(12) -> (48, 144, 16.970562748477143)
- square(7) -> (28, 49, 9.899494936611665)
"""

import math


def square(side: str) -> tuple:
    """Вычисляет периметр, площадь, диагональ квадрата по стороне

    :param side: сторона квадрата
    :type side: str

    :return: Кортеж (Периметр, Площадь, Диагональ)
    :rtype: tuple
    """
    side = float(side)
    perimeter = side * 4
    s_square = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, s_square, diagonal


if __name__ == '__main__':
    side_val = input('Введите сторону квадрата: ')
    print(f'(Периметр, Площадь, Диагональ): {square(side_val)}')
