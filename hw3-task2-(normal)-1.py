# coding: utf-8

# Normal

# Задание:
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000 (коррупция ведь), как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

import os


def longestLine(*args):
    return max(list(args), key=len)


names = ('Vasya', 'Ivan', 'Sergey', 'Mihail')
salaries = (5000, 500000, 500001, 0)

dictionary = dict(zip(names, salaries))
print(dictionary)

DIR = 'files'
path = os.path.join(DIR, 'salary.txt')  # хороший кроссплатформенный метод указания пути
wantedString = " - "

with open(path, 'w', encoding='UTF-8') as f:
    for key in dict.keys(dictionary):
        f.write(f'{key} - {dictionary[key]}\n')

with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if float(line[line.find(wantedString)+len(wantedString):]) <= 500000:
            print(f'{str.upper(line[:line.find(wantedString)])}{wantedString}{float(line[line.find(wantedString)+len(wantedString):])*0.87}')

input()
