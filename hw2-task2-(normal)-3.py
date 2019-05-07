# coding: utf-8

# Normal

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = 10
rndIntList = []

for i in range(0, n):
	rndIntList.append(random.randint(-99, 99))

print(rndIntList)
input()