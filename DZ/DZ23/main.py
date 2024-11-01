# Модкль 8, часть 2, задание 1 
# К уже реализованномуклассу«Автомобиль»добавьте 
# возможностьупаковкии распаковки данных с использованием json и pickle

import json

class Auto:
    def __init__(self):
        self.file_path = 'auto.json'
        self.Manufacturer = input('Введите производителя автомобиля: ')
        self.model = input('Введите марку автомобиля: ')
        self.year = input('Введите год автомобиля: ')
        self.engine = input('Введите объём двигателя: ')
        self.color = input('Введите цвет автомобиля: ')
        self.__price = input('Введите цену автомобиля: ')

    def save_auto(self):
        # Сохраняем данные автомобиля в формате JSON.
        data = {
            'Manufacturer': self.Manufacturer,
            'model': self.model,
            'year': self.year,
            'engine': self.engine,
            'color': self.color,
            'price': self.__price
        }
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)# Вот эту строчку не до конца понимаю, ну и в книге и стадионе ее же. 

    def display_info(self):

        print(f'Производитель: {self.Manufacturer}, Модель: {self.model}, '
              f'Год выпуска: {self.year}, Объем двигателя: {self.engine}, '
              f'Цвет: {self.color}, Цена: {self.__price}')

    def get_manufacturer(self):
        return self.Manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_engine(self):
        return self.engine

    def get_color(self):
        return self.color

    def get_price(self):
        return self.__price


if __name__ == "__main__":
    a = Auto()
    a.save_auto()
    print("\nДанные автомобиля:")
    a.display_info()


# Модуль 8, часть 2, задание 2 
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки
# данных с использованием json и pickle.

# import json


# class Book:
#     def __init__(self):
#         self.file_path = 'book.json'
#         self.name = input('Введите название книги: ')
#         self.publisher = input('Введите издателя книги: ')
#         self.year = input('Введите год выпуска книги: ')
#         self.genre = input('Введите жанр книги: ')
#         self.author = input('Введите автора книги: ')
#         self.__price = input('Введите цену книги: ')

#     def save_book(self):
#         data = {
#             'name': self.name,
#             'publisher': self.publisher,
#             'year': self.year,
#             'genre': self.genre,
#             'author': self.author,
#             'price': self.__price
#         }
#         with open(self.file_path, 'a', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=4)

#     def display_info(self):
#         print(f'Название книги: {self.name}, год выпуска: {self.year}, '
#               f'под издательством: {self.publisher}, жанр: {self.genre}, '
#               f'автор: {self.author}, по цене: {self.__price}')

#     def get_name(self):
#         return self.name

#     def get_year(self):
#         return self.year

#     def get_publisher(self):
#         return self.publisher

#     def get_genre(self):
#         return self.genre

#     def get_author(self):
#         return self.author

#     def get_price(self):
#         return self.__price

# if __name__ == "__main__":
#     a = Book()
#     a.save_book()
#     print("\nДанные о книге:")
#     a.display_info() 

# # Модуль8, чать 2, задание 3
# # К уже реализованному классу «Стадион» добавьте 
# # возможность упаковки и распаковки данных с исполь
# # зованием json и pickle.

# import json

# class Stadium:
#     def __init__(self):
#         self.file_path = 'stadium.json'
#         self.name = input('Введите название стадиона: ')
#         self.year = input('Введите год открытия: ')
#         self.country = input('Введите страну: ')
#         self.city = input('Введите город: ')
#         self.capacity = input('Введите вместимость: ')

#     def save_stadium(self):
#         data = {
#             'name': self.name,
#             'year': self.year,
#             'country': self.country,
#             'city': self.city,
#             'capacity': self.capacity
#        }
#         with open(self.file_path, 'a', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=4)

#     def display_info(self):
#         print(f'Название стадиона: {self.name}, открытый: {self.year}, '
#               f'В стране: {self.country}, городе: {self.city}, '
#               f'вместимостью: {self.capacity} человек')

# if __name__ == "__main__":
#     a = Stadium()
#     a.save_stadium()
#     print("\nДанные о стадионе:")
#     a.display_info() 






