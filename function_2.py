# В зависимости от выбора пользователя, вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
import math


def rect(a, b):
    return a * b


def circle(r):
    return math.pi * r ** 2


def triangle(a, b, c):
    sq = (a + b + c) / 2
    return math.sqrt(sq * (sq - a) * (sq - b) * (sq - c))


choice = input("Прямоугольник(r)', Круг(c), Треугольник(t): ")
if choice == "c":
    rad = int(input('Радиус'))
    print(f"Радиус круга : {circle(rad)} ")
elif choice == "r":
    sq_1 = int(input('Ширина -'))
    sq_2 = int(input('Длина -'))
    print(f"Площадь прямоугольника : {rect(sq_1,sq_2)}")
elif choice == "t":
    sq_t_1 = int(input('Первая сторона  -'))
    sq_t_2 = int(input('Вторая сторона  -'))
    sq_t_3 = int(input('Третья сторона  -'))
    print(f"Площадь треугольника : {triangle(sq_t_1,sq_t_2,sq_t_3)}")

