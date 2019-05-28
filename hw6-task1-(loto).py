# coding: utf-8

# Loto

# Задача:
# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

from random import randint
# from os import join as path_join
import os


class PlayerCard:
    def __init__(self, name):
        self._name = name
        self._player_card_list = ()
        self._player_card_num = 0
        self._player_card = ''
        self._player_card_line = ''
        self.make_new_player_card()

    def get_name(self):
        return self._name

    def get_player_card(self):
        return self._player_card

    def make_new_player_card(self):
        while len(_player_card_list) == 15:
            self._player_card_num = randint(1, 90)
            if self._player_card_num not in self._player_card_list:
                self._player_card_list.append(self._player_card_num)

        self._player_card = f'{self._name:-^{20 - len(self._name)}}'

        for i in range(0, 2):
            for j in range(1, 5):
                self._player_card_line += f'{self._player_card_list[i + j]} '

            self._player_card += f'\n{self._player_card_line}'
        self.player_card += f'\n{"":-^20}'


class Game:
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._moves = 90

    def start(self):
        for moves_left in self._moves:
            game_barrel = randint(1, 90)
            print(f'Новый бочонок: {game_barrel} (осталось {moves_left})')
            print(self._player1.get_player_card())
            print(self._player2.get_player_card())

            while True:
                continue_play = input('Зачеркнуть цифру? (y/n)')
                if continue_play == 'y':
                    pass
                elif continue_play == 'n':
                    break
                else:
                    print('Некорректный ввод')


player1 = PlayerCard('Ваша карточка')
player2 = PlayerCard('Карточка компьютера')
game = Game(player1, player2)
game.start()

input()
