# Модуль 10, задание 1 
# К уже реализованному классу «Дробь»
# добавьте статический метод,
# который при вызове возвращает 
# количество созданных объектов класса «Дробь».

class Fraction:
    def init(self, numerator: int, denominator: int, intpart: int = 0):
        self.num: int = numerator + intpart * denominator
        self.den: int = denominator

class Fraction:
    _instance_count = 0

    def __init__(self, numerator: int, denominator: int, int_part: int = 0):
        self.__num: int = numerator + int_part * denominator
        self.__den: int = denominator
        Fraction._instance_count += 1  # Увеличиваем счетчик при создании нового экземпляра

    @staticmethod
    def get_instance_count() -> int:
        return Fraction._instance_count  # Статический метод возвращает количество созданных объектов

    def add(self, fraction: 'Fraction') -> 'Fraction':
        num = self.__num * fraction.__den + fraction.__num * self.__den
        den = self.__den * fraction.__den
        return Fraction(num, den)

    def subtract(self, fraction: 'Fraction') -> 'Fraction':
        num = self.__num * fraction.__den - fraction.__num * self.__den
        den = self.__den * fraction.__den
        return Fraction(num, den)

    def multiply(self, fraction: 'Fraction') -> 'Fraction':
        num = self.__num * fraction.__num
        den = self.__den * fraction.__den
        return Fraction(num, den)

    def divide(self, fraction: 'Fraction') -> 'Fraction':
        num = self.__num * fraction.__den
        den = self.__den * fraction.__num
        return Fraction(num, den)

    def __str__(self) -> str:
        num = self.__num
        if self.__num > self.__den:
            int_part = self.__num // self.__den
            num -= int_part * self.__den
            return f'{int_part} ({num}/{self.__den})'
        elif self.__num == self.__den:
            return str(int(self.__num / self.__den))

        return f'{self.__num}/{self.__den}'

    def __float__(self) -> float:
        return self.__num / self.__den

f1: Fraction = Fraction(5, 7)
f2: Fraction = Fraction(1, 7)

f3: Fraction = f1.add(f2)
print(f3)  
print(float(f3))  

f4: Fraction = f1.subtract(f2)
print(f4)  
print(float(f4))  

f5: Fraction = f1.multiply(f2)
print(f5)  
print(float(f5))  

f6: Fraction = f1.divide(f2)
print(f6)  
print(float(f6))  

print("Количество созданных объектов Fraction:", Fraction.get_instance_count())  # 6 (включая все созданные экземпляры)


# Модуль 10, задание 2
# Создайте класс для конвертирования температуры из 
# Цельсия в Фаренгейт и наоборот. У класса должно быть 
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также 
# класс должен считать количество подсчетов температурыи 
# возвращать это значение с помощью статического метода.

class Conversion:
    count = 0  # Статическая переменная для учета количества преобразований

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        Conversion.count += 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        Conversion.count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_count():
        return Conversion.count



temp_c = 20  
temp_f = Conversion.celsius_to_fahrenheit(temp_c)
print(f"{temp_c} °C это {temp_f} °F")  # Преобразование из Цельсия в Фаренгейт

temp_f = 68  
temp_c = Conversion.fahrenheit_to_celsius(temp_f)
print(f"{temp_f} °F это {temp_c} °C")  # Преобразование из Фаренгейта в Цельсий

# Получение количества преобразований
print(f"Количество преобразований: {Conversion.get_count()}")


# Модуль 10, задание 3
# Создайте класс для перевода из метрической системы 
# в английскую и наоборот. Функциональность необходимо 
# реализовать в виде статических методов. Обязательно 
# реализуйте перевод мер длины

class Metric_converter:
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28
        return(feet)
    
    @staticmethod
    def feet_to_meters(feet):
        meters = feet / 3.28
        return(meters)
    
meters = 10
feet = Metric_converter.meters_to_feet(meters)
print(f'{meters} метров = {feet} футов')

feet = 50
meters = Metric_converter.feet_to_meters(feet)
print(f'{feet} футов = {meters} метров')

        
 
 
 
 
 
 
