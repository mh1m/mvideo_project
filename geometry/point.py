import numpy as np

from math import sqrt


"""
Класс соответствующий точке в пространстве
"""
class Point:

    """
    Конструктор класса
    @in x - координата x точки
    @in y - координата y точки
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Перегружаем оператор сложения
    @in other - точка
    @return - точка
    """
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    """
    Перегружаем оператор вычитания
    @in other - точка
    @return - точка
    """
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    """
    Перегружаем оператор умножения на константу
    @in other - константа
    @return - точка
    """
    def __mul__(self, coeff: float):
        return Point(coeff * self.x, coeff * self.y)

    """
    Расстояние между двумя точками. Статический метод
    @in first - точка Point
    @in secon - точка Point
    @return double - расстояние между ними
    """
    @staticmethod
    def distance(first, second):
        return sqrt((first.x - second.x) ** 2 + (first.y - second.y) ** 2)

    """
    Линейная интерполяция
    @in A - начальное значение
    @in B - конечное значение
    @in t float - коэффициент линейной интерполяции
    @return tuple
    """
    @staticmethod
    def lerp(A, B, t: float):
        if t > 1:
            t = 1
        elif t < 0:
            t = 0

        return tuple(np.add(A, t * np.subtract(B, A)))

    """
    Скалярное произведение векторов
    @in other - точка
    @return float - скалярное произведение
    """
    def scalarProduct(self, other):
        return self.x * other.x + self.y * other.y

    """
    Расстояние от данной точки до отрезка
    @in P0 - первая точка отрезка
    @in P1 - вторая точка отрезка
    @return float - расстояние
    """
    def distanceSegment(self, P0, P1) -> float:
        v = P1 - P0
        w = self - P0
        c1 = w.scalarProduct(v)
        if c1 <= 0:
            return self.distance(self, P0)
        c2 = v.scalarProduct(v)
        if c2 <= c1:
            return self.distance(self, P1)
        b = c1 / c2
        pPerp = P0 + w * b
        return self.distance(self, pPerp)


