# Задача 5: Магические методы
# Описание: Создайте класс ComplexNumber, который будет представлять комплексное число и реализуйте сложение и вычитание комплексных чисел, используя магические методы add() и sub().
# Условия:
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.


import math

class Complex:
    def __init__(self, real: float, im: float):
        self.__real: float = real
        self.__im: float = im

    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.__real + other.__real, self.__im + other.__im)

    def __sub__(self, other: 'Complex') -> 'Complex':
        return Complex(self.__real - other.__real, self.__im - other.__im)

    def __str__(self) -> str:
        sign = '+' if self.__im >= 0 else '-'
        return f'{self.__real} {sign} i{math.fabs(self.__im)}' if self.__im != 0 else str(self.__real)

a = Complex(1, 5)
b = Complex(2, -3)
c = a + b
d = a - b

print(a)  
print(b)  
print(c)  
print(d)   


# адача 6: Инкапсуляция
# Описание: Создайте класс Car, который содержит информацию о марке автомобиля, максимальной скорости и текущей скорости.
#  Инкапсулируйте переменные с текущей скоростью, чтобы нельзя было напрямую её изменять.
# Условия:
#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя, чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.


class Car:
    def __init__(self, brand: str, maximum_speed: int, current_speed: int = 0):
        self.brand: str = brand
        self.maximum_speed: int = maximum_speed
        self.__current_speed: int = current_speed

    def increase_speed(self):
        if self.__current_speed < self.maximum_speed:
            self.__current_speed += 10
            if self.__current_speed > self.maximum_speed:
                self.__current_speed = self.maximum_speed  # Ограничение скорости
        else:
            print('Скорость уже максимальная')

    def decrease_in_speed(self):
        if self.__current_speed <= 0:
            print('Вы стоите ;D')
        else:
            self.__current_speed -= 10
            if self.__current_speed < 0:
                self.__current_speed = 0  # Убедимся, что скорость не ниже нуля

    def current_speed(self) -> int:
        return self.__current_speed

    def __str__(self) -> str:
        return f'Машина, брендом: {self.brand},\n с максимальной скоростью: {self.maximum_speed} и текущей скоростью: {self.__current_speed}'


res = Car('AUDI', 250, 120)
res.increase_speed()
print(res)

res.decrease_in_speed()
print(res)


# Задача 7: Абстрактные классы
# Описание: Создайте абстрактный класс Shape, который имеет абстрактный метод get_area().
#  Затем создайте классы Square и Triangle, которые наследуются от этого абстрактного класса
#  и реализуют свои версии метода get_area().
# Условия:
#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.
# Каждая из этих задач поможет вам лучше понять принципы ООП, такие как инкапсуляция, наследование, полиморфизм и абстракция.

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length: int = length

    def get_area(self):
        return self.length * self.length

    def __str__(self) -> str:
        return f'Квадрат, с длинами сторон: {self.length}, площадь равна: {self.get_area()}'

class Triangle(Shape):
    def __init__(self, name: str, base: int, height: int):
        super().__init__(name)
        self.base: int = base
        self.height: int = height

    def get_area(self):
        return (self.height * self.base) / 2

    def __str__(self) -> str:
        return f'Треугольник, с основанием: {self.base} и высотой: {self.height}, площадь равна: {self.get_area()}'

res_square = Square('Квадрат', 10)
print(res_square)

res_triangle = Triangle('Треугольник', 10, 8)
print(res_triangle)