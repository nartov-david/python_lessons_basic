# coding: utf-8

# Hard

# # Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# # Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# # вычислите и выведите y

print('Здравствуйте!')

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))
weight = int(input('Введите ваш вес: '))

if age > 40 and (weight < 50 or weight > 120):
	print(name, surname + ', ' + str(age) + ' год, вес ' + str(weight) + ' - следует обратится к врачу!')
elif age > 30 and (weight < 50 or weight > 120):
	print(name, surname + ', ' + str(age) + ' год, вес ' + str(weight) + ' - следует заняться собой')
elif age < 30 and (weight > 50 or weight < 120):
	print(name, surname + ', ' + str(age) + ' год, вес ' + str(weight) + ' - хорошее состояние')
else:
	print('Что ты !?')

input()