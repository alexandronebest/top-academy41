# Модуль 12, часть 1, задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

# Не особо понял, что конкретно нужно реализовать, вот пример испольщования паттерна Builder:
# Сейчас попробую во втором задание его реализовать. 



# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any


# class Builder(ABC):
#     """
#     Интерфейс Строителя объявляет создающие методы для различных частей объектов
#     Продуктов.
#     """

#     @property
#     @abstractmethod
#     def product(self) -> None:
#         pass

#     @abstractmethod
#     def produce_part_a(self) -> None:
#         pass

#     @abstractmethod
#     def produce_part_b(self) -> None:
#         pass

#     @abstractmethod
#     def produce_part_c(self) -> None:
#         pass


# class ConcreteBuilder1(Builder):
#     """
#     Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
#     конкретные реализации шагов построения. Ваша программа может иметь несколько
#     вариантов Строителей, реализованных по-разному.
#     """

#     def __init__(self) -> None:
#         """
#         Новый экземпляр строителя должен содержать пустой объект продукта,
#         который используется в дальнейшей сборке.
#         """
#         self.reset()

#     def reset(self) -> None:
#         self._product = Product1()

#     @property
#     def product(self) -> Product1:
#         """
#         Конкретные Строители должны предоставить свои собственные методы
#         получения результатов. Это связано с тем, что различные типы строителей
#         могут создавать совершенно разные продукты с разными интерфейсами.
#         Поэтому такие методы не могут быть объявлены в базовом интерфейсе
#         Строителя (по крайней мере, в статически типизированном языке
#         программирования).

#         Как правило, после возвращения конечного результата клиенту, экземпляр
#         строителя должен быть готов к началу производства следующего продукта.
#         Поэтому обычной практикой является вызов метода сброса в конце тела
#         метода getProduct. Однако такое поведение не является обязательным, вы
#         можете заставить своих строителей ждать явного запроса на сброс из кода
#         клиента, прежде чем избавиться от предыдущего результата.
#         """
#         product = self._product
#         self.reset()
#         return product

#     def produce_part_a(self) -> None:
#         self._product.add("PartA1")

#     def produce_part_b(self) -> None:
#         self._product.add("PartB1")

#     def produce_part_c(self) -> None:
#         self._product.add("PartC1")


# class Product1():
#     """
#     Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
#     достаточно сложны и требуют обширной конфигурации.

#     В отличие от других порождающих паттернов, различные конкретные строители
#     могут производить несвязанные продукты. Другими словами, результаты
#     различных строителей могут не всегда следовать одному и тому же интерфейсу.
#     """

#     def __init__(self) -> None:
#         self.parts = []

#     def add(self, part: Any) -> None:
#         self.parts.append(part)

#     def list_parts(self) -> None:
#         print(f"Product parts: {', '.join(self.parts)}", end="")


# class Director:
#     """
#     Директор отвечает только за выполнение шагов построения в определённой
#     последовательности. Это полезно при производстве продуктов в определённом
#     порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
#     так как клиент может напрямую управлять строителями.
#     """

#     def __init__(self) -> None:
#         self._builder = None

#     @property
#     def builder(self) -> Builder:
#         return self._builder

#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#         """
#         Директор работает с любым экземпляром строителя, который передаётся ему
#         клиентским кодом. Таким образом, клиентский код может изменить конечный
#         тип вновь собираемого продукта.
#         """
#         self._builder = builder

#     """
#     Директор может строить несколько вариаций продукта, используя одинаковые
#     шаги построения.
#     """

#     def build_minimal_viable_product(self) -> None:
#         self.builder.produce_part_a()

#     def build_full_featured_product(self) -> None:
#         self.builder.produce_part_a()
#         self.builder.produce_part_b()
#         self.builder.produce_part_c()


# if __name__ == "__main__":
#     """
#     Клиентский код создаёт объект-строитель, передаёт его директору, а затем
#     инициирует процесс построения. Конечный результат извлекается из объекта-
#     строителя.
#     """

#     director = Director()
#     builder = ConcreteBuilder1()
#     director.builder = builder

#     print("Standard basic product: ")
#     director.build_minimal_viable_product()
#     builder.product.list_parts()

#     print("\n")

#     print("Standard full featured product: ")
#     director.build_full_featured_product()
#     builder.product.list_parts()

#     print("\n")

#     # Помните, что паттерн Строитель можно использовать без класса Директор.
#     print("Custom product: ")
#     builder.produce_part_a()
#     builder.produce_part_b()
#     builder.product.list_parts()




# Модуль 12, часть 1, задание 2 
# Создайтеприложениедляприготовленияпасты.При
# ложение должноуметьсоздавать минимумтривидапа
# сты.  Классыразличнойпастыдолжныиметьследующие 
# методы:
#  ■ Тип пасты;
#  ■ Соус;
#  ■ Начинка;
#  ■ Добавки.
#  Дляреализациииспользуйтепорождающиепаттерны.

class Pasta:
    def __init__(self, pasta_type: str, sauce: str, filling: str, add_ons: list):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.filling = filling
        self.add_ons = add_ons

    def __str__(self) -> str:
        return (f'Паста: {self.pasta_type}, Соус: {self.sauce} '
                f'Начинка: {self.filling}, с добавкой: {", ".join(self.add_ons)}')


class Spaghetti(Pasta):
    def __init__(self, sauce: str, filling: str, add_ons: list):
        super().__init__('Спагетти', sauce, filling, add_ons)


class Penne(Pasta):
    def __init__(self, sauce: str, filling: str, add_ons: list):
        super().__init__('Пенне', sauce, filling, add_ons)


class Fettuccine(Pasta):
    def __init__(self, sauce: str, filling: str, add_ons: list):
        super().__init__('Феттучини', sauce, filling, add_ons)


class PastaBuilder:
    def __init__(self):
        self.pasta_type = None
        self.sauce = None
        self.filling = None
        self.add_ons = []

    def set_type(self, pasta_type: str):
        self.pasta_type = pasta_type
        return self

    def set_sauce(self, sauce: str):
        self.sauce = sauce
        return self

    def set_filling(self, filling: str):
        self.filling = filling
        return self

    def add_adding(self, add_on: str):
        self.add_ons.append(add_on)
        return self

    def build(self):
        if self.pasta_type == 'Спагетти':
            return Spaghetti(self.sauce, self.filling, self.add_ons)
        elif self.pasta_type == 'Пенне':
            return Penne(self.sauce, self.filling, self.add_ons)
        elif self.pasta_type == 'Феттучини':
            return Fettuccine(self.sauce, self.filling, self.add_ons)
        else:
            raise ValueError('Такого типа пасты нет')


if __name__ == '__main__':
    spaghetti = (PastaBuilder()
                  .set_type('Спагетти')
                  .set_sauce('Сырный соус')
                  .set_filling('Мясная начинка')
                  .add_adding('Лук')
                  .build())

    print(spaghetti)

    fettuccine = (PastaBuilder()
                  .set_type('Феттучини')
                  .set_sauce('Чесночный')
                  .set_filling('Куриная начинка')
                  .add_adding('Оливки')
                  .build())

    print(fettuccine)


# Модуль 12, часть 1, задание 3
# Создайте реализацию паттерна Prototype. 
# Протестируйте работу созданного класса.

import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototypeA(Prototype):
    def __init__(self, fileid1, fileid2):
        self.fileid1 = fileid1
        self.fileid2 = fileid2

    def __str__(self):
        return f'ConcretePrototypeA(fileid1 = {self.fileid1}, fileid2 = {self.fileid2})'


class ConcretePrototypeB(Prototype):
    def __init__(self, fileid3, fileid4):
        self.fileid3 = fileid3
        self.fileid4 = fileid4

    def __str__(self):
        return f'ConcretePrototypeB(fileid3 = {self.fileid3}, fileid4 = {self.fileid4})'

# Тестируем
def main():
    # Создаем оригинальные объекты
    prototype_a1 = ConcretePrototypeA("1111", "2222")
    prototype_b1 = ConcretePrototypeB("3333", "4444")

    print("Оригинальные объекты:")
    print(prototype_a1)
    print(prototype_b1)

    # Клонируем объекты
    prototype_a2 = prototype_a1.clone()
    prototype_b2 = prototype_b1.clone()

    print("\n Клонированные объекты:")
    print(prototype_a2)
    print(prototype_b2)

    # Изменяем клонированные объекты
    prototype_a2.fileid1 = "new_1111"
    prototype_b2.fileid3 = "new_3333"

    print("\n После изменения клонированных объектов:")
    print(prototype_a1)
    print(prototype_a2)
    print(prototype_b1)
    print(prototype_b2)

if __name__ == "__main__":
    main()
