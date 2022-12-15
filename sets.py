from random import randint
import random
number_of_set = []
number_of_sets = int(input('Введите количество множеств'))
for i in range(number_of_sets):
    j = set((random.randint(1, 50)) for y in range(number_of_sets))
    number_of_set.append(j)
print(number_of_set)