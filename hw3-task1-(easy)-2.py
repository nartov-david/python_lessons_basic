# coding: utf-8

# Easy

# Задание - 2:
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def maxNum(num1, num2, num3):
    return max(num1, num2, num3)


number1 = int(input('Введите 1-ое число: '))
number2 = int(input('Введите 2-ое число: '))
number3 = int(input('Введите 3-ье число: '))

print(maxNum(number1, number2, number3))

input()
