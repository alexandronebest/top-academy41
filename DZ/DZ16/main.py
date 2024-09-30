# Модуль 10, задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс
# CofeeMachine (содержит информацию о кофемашине),
# класс Blender(содержит информацию о блендере), класс
# класс Blender (содержит информацию о блендере), класс 
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые 
# для работы методы.


class Device:
    def __init__(self, name: str, price: int):
        self._name:str = Device._validate_name(name)
        self._price:int = Device._validate_price(price)

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return(name)
        raise Exception('Имя должно содержать только буквы')


    @staticmethod
    def _validate_price(price: int) -> int:
        if price > 0:
            return(price)
        
    
    def __str__(self) -> str:
        return f'{self._name}, {self._price}'
        

class CofeeMachine(Device):
    def __init__(self, name: str, price: int, number_of_types_of_coffee: int):
        super().__init__(name, price)
        self.number_of_types_of_coffee = number_of_types_of_coffee


    def is_number_of_types_of_coffee(self):
        if self.number_of_types_of_coffee < 0:
            return False
        

    def __str__(self) -> str:
        return f'Название кофемашины:{self._name}, по цене:{self._price}, изготавливает видов кофе:{self.number_of_types_of_coffee}'


class Blender(Device):
    def __init__(self, name: str, price: int, blender_power: int):
        super().__init__(name, price)
        self.blender_power = blender_power


    def is_blender_power(self):
        if self.blender_power < 0:
            return False
        

    def __str__(self) -> str:
        return f'Название блендэра: {self._name}, по цене: {self._price}, с мощностью: {self.blender_power} Вт'


class MeatGrinder(Device):
    def __init__(self, name: str, price: int, meat_grinder_rpm: int):
        super().__init__(name, price)
        self.meat_grinder_rpm = meat_grinder_rpm

    def is_meat_grinder_rpm(self):
        if self.meat_grinder_rpm < 0:
            return False
        

    def __str__(self) -> str:
        return f'Название мясорубки: {self._name}, по цене: {self._price}, с количеством: {self.meat_grinder_rpm} Об/мин'


d1 = CofeeMachine('CofeeMachine', 5000, 3)
print(d1)

d2 = Blender('blender', 2500, 1000)
print(d2)

d3 = MeatGrinder('MeatGrinder', 3899, 1500)
print(d3)
    

# Модуль 10, задание 2
# Создайте класс Ship, который содержит информацию 
# о корабле.
# С помощью механизма наследования, реализуйте 
# класс Frigate (содержит информацию о фрегате), класс 
# Destroyer (содержит информацию об эсминце), класс 
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые 
# для работы методы.


class Ship:
    def __init__(self, name: str, passengers: int):
        self._name:str = Ship._validate_name(name)
        self._passengers:int = Ship._validate_passengers(passengers)

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return(name)
        raise Exception('Имя должно содержать только буквы')


    @staticmethod
    def _validate_passengers(passengers: int) -> int:
        if passengers > 0:
            return(passengers)
        

    def __str__(self) -> str:
        return f'Корабль: {self._name}, Вместимость : {self._passengers} человек.'


class Frigate(Ship):
    def __init__(self, name: str, passengers: int, length: int):
        super().__init__(name, passengers)
        self.lenght = length 


    def __str__(self) -> str:
        return f'Название:{self._name}, количество челенов  команды: {self._passengers} человек, длинной: {self.lenght}м.'

class Destroyer(Ship):
    def __init__(self, name: str, passengers: int, mine: int):
        super().__init__(name, passengers)
        self.mine = mine


    def __str__(self) -> str:
        return f'Название:{self._name}, количество членов команды:{self._passengers} человек, вооружён: {self.mine} минами'

class Cruiser(Ship):
    def __init__(self, name: str, passengers: int, speed: int):
        super().__init__(name, passengers)
        self.speed = speed


    def __str__(self) -> str:
        return f'Название:{self._name}, количество членов команды:{self._passengers} человек, скорость: {self.speed} узлов'






k1 = Ship('SantaMaria', 40)
print(k1)

k2 = Frigate('Frigate', 100, 135)
print(k2)

k3 = Destroyer('Destroyer', 337, 34)
print(k3)

k4 = Cruiser('Cruiser', 40, 30)
print(k4)


# Модуль 10, задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и 
# поле для хранения копеек (центы, евроценты, копейки 
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.      


class Money:
    def __init__(self, dollar: int, euro: int, ruble: int, cent: int, eurocent: int, kopeck: int):
        self.dollar = dollar
        self.euro = euro
        self.ruble = ruble
        self.cent = cent
        self.eurocent = eurocent
        self.kopeck = kopeck


    def input_money(self):
        self.dollar = int(input('Введите количество долларов: '))
        self.euro = int(input('Введите количество евро: '))
        self.ruble = int(input('Введите количество рублей: '))
        self.cent = int(input('Введите количество центов: '))
        self.eurocent = int(input('Введите количество евроцентов: '))
        self.kopeck = int(input('Введите количество копеек: '))


    def __str__(self):
        return (f'У вас денег:\n'
                f'Долларов - {self.dollar} и {self.cent} центов,\n'
                f'Евро - {self.euro} и {self.eurocent} евроцентов,\n'
                f'Рублей - {self.ruble} и {self.kopeck} копеек.')


res = Money(0, 0, 0, 0, 0, 0)
res.input_money()
print(res)
