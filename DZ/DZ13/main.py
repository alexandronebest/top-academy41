# Модуль 10, часть 1, задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить 
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте 
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 

# class Auto:
#         def __init__(self):
#             with open('auto.txt', 'r', encoding='utf-8') as f:
#                lines = f.readlines()
#                self.Manufacturer = input('Введите производителя автомобиля')
#                self.model = input('Введите марку автомобиля')
#                self.year = input('Введите год автомобиля') 
#                self.engine = input('Введите объём двигателя')
#                self.color = input('Введите цвет автомобиля')
#                self.price = input('Введите цену автомобиля')


#         def save_auto(self):
#               with open('auto.txt', 'a', encoding='utf-8') as f:
#                   f.write(f'Производитель:{self.Manufacturer} Модель:{self.model}, год выпуска:{self.year}, объем двигателя:{self.engine}, цвет:{self.color}, цена: {self.price}\n')
                   
                   
#         def display_info(self):
#              print(f'Производитель:{self.Manufacturer} Модель:{self.model}, год выпуска:{self.year}, объем двигателя:{self.engine}, цвет:{self.color}, цена: {self.price}\n')


#         def get_manufacturer(self):
#              return(self.Manufacturer)
        
        
#         def get_model(self):
#              return(self.model)
        
        
#         def get_year(self):
#              return(self.year)
        
        
#         def get_engine(self):
#              return(self.engine)
        
        
#         def get_color(self):
#              return(self.color)
        

#         def get_price(self):
#              return(self.price)


# if __name__ == "__main__":
#     a = Auto()
#     a.save_auto()
#     print("\\nДанные автомобиля:")
#     a.display_info()              


# Модуль 10, часть 1, задание 2
# Реализуйте класс «Книга». Необходимо хранить в 
# полях класса: название книги, год выпуска, издателя, 
# жанр, автора, цену. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса
          
# class Book:
#         def __init__(self):
#             with open('book.txt', 'r', encoding='utf-8') as f:
#                lines = f.readlines()
#                self.name = input('Введите название книги')
#                self.year = input('Введите год выпуска книги') 
#                self.publisher = input('Введите издателя книги')
#                self.genre = input('Введите жанр книги')
#                self.author = input('Введите автора книги')
#                self.price = input('Введите цену книги')


#         def save_book(self):
#               with open('book.txt', 'a', encoding='utf-8') as f:
#                   f.write(f'Название книги:{self.name}, год выпуска:{self.year}, под издательством:{self.publisher}, жанр:{self.genre}, автор:{self.author}, по цене: {self.price}\n')
                   
                   
#         def display_info(self):
#              print(f'Название книги:{self.name}, год выпуска:{self.year}, под издательством:{self.publisher}, жанр:{self.genre}, автор:{self.author}, по цене: {self.price}\n')

#         def get_name(self):
#              return(self.name)
        
        
#         def get_year(self):
#              return(self.year)
        
        
#         def get_publisher(self):
#              return(self.publisher)
        
        
#         def get_genre(self):
#              return(self.genre)
        
        
#         def get_author(self):
#              return(self.author)
        

#         def get_price(self):
#              return(self.price)


# if __name__ == "__main__":
#     a = Book()
#     a.save_book()
#     print("\\nДанные о книге:")
#     a.display_info()            


# Модуль 10, часть 1, задание 3
# Реализуйте класс «Стадион». Необходимо хранить в 
# полях класса: название стадиона, дату открытия, страну, 
# город, вместимость. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса

class Stadium:
        def __init__(self):
            with open('stadium.txt', 'r', encoding='utf-8') as f:
               lines = f.readlines()
               self.name = input('Введите название стадиона')
               self.year = input('Введите год дату открытия') 
               self.country = input('Введите страну') 
               self.city = input('вВведите город')
               self.capacity = input('Введите вместимость')



        def save_stadium(self):
              with open('stadium.txt', 'a', encoding='utf-8') as f:
                  f.write(f'Название стадиона:{self.name}, открытый:{self.year}, в стране:{self.country}, городе:{self.city}, вместимостью:{self.capacity} человек\n')
                   
                   
        def display_info(self):
             print(f'Название стадиона:{self.name}, открытый:{self.year}, в стране:{self.country}, городе:{self.city}, вместимостью:{self.capacity} человек\n')

        def get_name(self):
             return(self.name)
        
        
        def get_year(self):
             return(self.year)
        
        
        def get_country(self):
             return(self.country)
        
        
        def get_city(self):
             return(self.city)
        
        
        def get_capacity(self):
             return(self.capacity)
        


if __name__ == "__main__":
    a = Stadium()
    a.save_stadium()
    print("\\nДанные о стадионе:")
    a.display_info() 

