# Задача 3. Неправильный код

import random


def change(nums):
    nums = list(nums)
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    nums = tuple(nums)

    return nums, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)

print(new_nums, rand_val)

new_nums, tmp = change(new_nums)

rand_val += tmp

print(new_nums, rand_val)
