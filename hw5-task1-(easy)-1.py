# coding: utf-8

# Easy

# Задание - 1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def make_dir(dir_name):
    if not dir_name:
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'Директория {dir_name} создана')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')


def remove_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print(f'Директория {dir_name} удалена')
    except PermissionError:
        print(f'Отказано в доступе: {dir_name}')
    except FileNotFoundError:
        print(f'Директория {dir_name} не существует')


while True:
    what_to_do = input(
        '''Для создания директорий "dir_1 - dir_9" - введите "m";
для удаления директорий "dir_1 - dir_9" - введите "r":
для выхода - введите "q": ''')
    if what_to_do == 'm':
        for n in range(1, 10):
            make_dir(f'dir_{n}')
        print()
        break
    elif what_to_do == 'r':
        for n in range(1, 10):
            remove_dir(f'dir_{n}')
        print()
        break
    elif what_to_do == 'q':
        print(f'{what_to_do} - неизвестная команда')
        break
    else:
        print(f'{what_to_do} - неизвестная команда\n')
        pass

input()
