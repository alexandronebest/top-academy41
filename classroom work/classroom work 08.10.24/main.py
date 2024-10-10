# Описание: Создайте класс Book, который будет содержать информацию о книге 
# (название, автор, год издания). 
# Создайте методы для отображения информации о книге и для изменения года издания.

# class Book:
#     def __init__(self, name: str, author: str, year: int):
#         self.name = name
#         self.author = author
#         self.year = year
#     def change_of_year(self, change_of_year -> int):
#         self.change_of_year = change_of_year
        
#     def __str__(self) -> str:
#         return(f'{self.name},{self.author}, {self.year},')
        
# res = Book('Гарри Поттер','Роулинг', 1998)
# print(res)

# Book.change_of_year()




# Описание: Создайте класс BankAccount, который будет моделировать банковский счёт. В классе должны быть методы для пополнения счёта, 
# снятия денег и вывода текущего баланса.

# Условия:

#  • Конструктор должен принимать начальный баланс.
#  • Метод deposit(amount) для пополнения счёта.
#  • Метод withdraw(amount) для снятия средств (не должно быть возможности уйти в минус).
# #  • Метод get_balance() для отображения текущего баланса.

# class BankAccount:
#    def __init__(self, balance:int):
#     self.balance = balance

#     def __str__(self) -> str:
#         return self.balance
    
#     def account_replenishment(self):
#         account_replenishment = int (input('Сколько добавить к балансу?'))
#         account_replenishment + self.balance

#     def withdrawal_from_account(self):
#         withdrawal_from_account = int(input('Введите сумму снятия'))
#         self.balance - withdrawal_from_account


    
# res = 100
# print(res)

# Задача 3: Наследование

# Описание: Создайте класс Person, который будет хранить информацию о человеке (имя и возраст),
#  и класс Student, который наследуется от Person. В классе Student должны быть добавлены поля для хранения учебного заведения и среднего балла.

# Условия:

#  • Конструктор класса Person должен принимать имя и возраст.
#  • Конструктор класса Student должен дополнительно принимать учебное заведение и средний балл.
#  • Добавьте методы для отображения информации о студенте.



# class Person:
#     def __init__(self, name: str, age: int,):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return (f'Имя:{self.name}, возраст: {self.age},')


# class Student(Person):
#     def __init__(self, name: str, age: int, educational_institution: str, gpa: int):
#         super().__init__(name, age)
#         self.educational_institution = educational_institution
#         self.gpa = gpa
    
#     def __str__(self) -> str:
#         return (f'Имя:{self.name}, возраст: {self.age}, учебное заведение {self.educational_institution}, средний бал: {self.gpa}')





# res1 = Person('Alexandr', 28)
# print(res1)
# res2= Student('Alexey', 30, 'Irgups', 4.7)
# print(res2)


# Задача 4: Полиморфизм

# Описание: Создайте классы Rectangle и Circle. Оба класса должны иметь метод get_area(), который возвращает площадь фигуры. Реализуйте механизм полиморфизма, который позволяет вызвать метод get_area() для объекта любого класса.

# Условия:

#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.


from abc import abstractmethod

class Rectangle:
    def __init__(self, Length: int, width: int):
        self.lenght = Length
        self.width = width

@abstractmethod
def get_area(self):
