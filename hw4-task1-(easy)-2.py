# coding: utf-8

# Easy

# Задание - 2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["банан", "киви", "арбуз"]
fruits2 = ["яблоко", "банан", "арбуз"]

new_list = [item for item in fruits1 if item in fruits2]
print(new_list)

input()
