# Написать функцию, которая определяет количество разрядов введённого целого числа.
def disc(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

num = int(input('Введите число'))
print('Количество разрядов', disc(num))



