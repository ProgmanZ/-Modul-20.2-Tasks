# Задача 1. Создание кортежей

import random


one_tuple = (random.randint(0, 6) for _ in range(10))
two_tuple = (random.randint(-5, 1) for _ in range(10))
three_tuple = tuple(list(one_tuple) + list(two_tuple))
print(three_tuple)
print((three_tuple.count(0)))

