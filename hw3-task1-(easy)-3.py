# coding: utf-8

# Easy

# Задание - 3:
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def longestLine(*args):
    return max(list(args), key=len)


arg1 = 'первый строковый аргумент'
arg2 = 'второй строковый аргумент'
arg3 = 'третий, самый длинный строковый аргумент'

print(longestLine(arg1, arg2, arg3))

input()
