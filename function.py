# Написать функцию, которая заполняет массив случайными числами в диапазоне,
# указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец,
# при этом ничего не возвращать.
# Вывод значений элементов массива должен происходить в основной ветке программы.
from random import randint
number_of_list = 10


def func(max_1, min_1):
    for i in range(number_of_list):
        a[i] = randint(max_1, min_1)


a = [0] * number_of_list
start = int(input())
end = int(input())
func(start, end)
print(a)
