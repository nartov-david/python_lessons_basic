# coding: utf-8

# Easy

# Задача - 1:
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
#
# Задача - 2:
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, car_name):
        self.speed = 0
        self.color = 'The color is not defined'
        self.name = car_name
        self.is_police = False

        self.car_is_moving = False
        self.car_moving_direction = 'f'

    def go(self):
        self.car_is_moving = True
        print('Машина поехала')

    def stop(self):
        self.car_is_moving = False
        print('Машина остановилась')

    def turn_direction(self):
        while True:
            self.car_moving_direction = input('Куда едем? "l"-налево, "r"-направо, "f"-прямо, "b"-задний ход: ')
            if self.car_moving_direction == 'l':
                print(f'Машина повернула (налево)')
            elif self.car_moving_direction == 'r':
                print(f'Машина повернула (направо)')
            elif self.car_moving_direction == 'f':
                print(f'Машина проехала (прямо)')
            elif self.car_moving_direction == 'b':
                print(f'Машина сдаёт назад (задний ход)')
            else:
                print(f'Неверная команда управления!')
                break


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, car_name):
        super().__init__(car_name)
        self.is_police = True

my_car_1 = Car('lada-2114')

my_car_1.go()
my_car_1.turn_direction()
my_car_1.stop()

input()
