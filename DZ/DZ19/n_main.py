# Модуль 14, часть 1, задание 1
# ользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип 
# списка нужно выбрать в зависимости от поставленной 
# ниже задачи). После чего нужно показать меню, в котором 
# предложить пользователю набор пунктов: 
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь 
# вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала 
# или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все 
# вхождения).
# В зависимости от выбора пользователя выполняется 
# действие, после чего меню отображается снова.


# def display_menu():
#     print('Меню:\n1- Добавить новое число\n2- Удалить все вхождения числа\n3- Показать содержимое числа\n4- Проверить есть ли значение в списке\n5- Заменить значение в списке\n6- Выхлд')

# def main():
#     numbers = []

#     while True:
#         display_menu()
#         choice = input('Выберите пункт меню (1-6):')
#         if choice == '1':
#             number = input("Введите число для добавления: ")
#             if number in numbers:
#                 print("Это число уже существует в списке.")
#             else:
#                 numbers.append(number)
#                 print(f"Число {number} добавлено в список.")
#         elif choice =='2':
#             number = input('Ввежите число для удаления')
#             count = numbers.count(numbers)
#             if count == 0:
#                 print('Число не найдето в списке')
#             else:
#                 numbers = [num for num in numbers if num != number]
#                 print(f'Число{number} удалены')
#         elif choice == '3':
#             choice_of_direction = input('Показать список с начала,введите 1 или с конца,введите 2 ')
#             if choice_of_direction == '1':
#                 print(f'Список с начала{numbers}')
#             elif choice_of_direction == '2':
#                 print(f'Список с конца{numbers[::-1]}')
#             else:
#                 print('Попробуйте ещё')
#         elif choice =='4':
#             number = input('Введите число для проверки:')
#             if number in numbers:
#                 print('Число найдено')
#             else:
#                 print('Число не найдено')
#         elif choice == '5':
#             old_number = input('Введите число для замены')
#             if old_number not in numbers:
#                 print('Число не найдено')
#                 continue

#             naw_number = input('Введите новое число')
#             replays_number = input('Заменить все вхождения введите 1, если нет то 2')
#             if replays_number.lower() == '1':
#                 numbers = [naw_number if num == old_number else num for num in numbers]
#                 print(f"Все вхождения числа {old_number} заменены на {naw_number}.")
#             else:
#                 index = numbers.index(old_number)
#                 numbers[index] = naw_number
#                 print(f"Первое вхождение числа {old_number} заменено на {naw_number}.")
#         elif choice == '6':
#             print('Выход')
#             break

#         else:
#             print('Попробуйте ещё')

# if __name__ == "__main__":
#     main()


# Модуль 14, часть 1, задание 2
# Реализуйте класс стека для работы со строками (стек 
# строк). 
# Стек должен иметь фиксированный размер. 
# Реализуйте набор операций для работы со стеком: 
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки 
# из стека.
# При старте приложения нужно отобразить меню с 
# помощью, которого пользователь может выбрать необходимую операцию.

# class StringStack:
#     def __init__(self, size):
#         self.stack = []
#         self.size = size

#     def push (self, string):
#         if len(self.stack) < self.size:
#             self.stack.append(string)
#         else:
#             print('Стек полон')

#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             print('Стек пуст')

#     def count(self):
#         return len(self.stack)
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def is_full(self):
#         return len(self.stack) == self.size
    
#     def clrar(self):
#         self.stack = []

#     def top(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None
        
# stack_size = int(input('Введите размер стека:'))
# stack = StringStack(stack_size)

# while True:
#     print('1. Поместить строку в стек')
#     print('2. Вытащить строку из стека')
#     print('3. Количество строк в стеке')
#     print('4. Проверить пустой ли стек')
#     print('5. Проверить полный ли стек')
#     print('6. Очистить стек')
#     print('7. Получить значение верхней строки стека')
#     print('0. Выход')

#     choise = input('Выбирите операцию')
#     if choise == '1':
#         string = input('Введите строку')
#         stack.push(string)
#     elif choise == '2':
#         poped_string = stack.pop()
#         if poped_string:
#             print(f'Извлеченная строка: {poped_string}')
#     elif choise == '3':
#         print (f'Количество строк в стеке: {stack.count()}')
#     elif choise == '4':
#         print(f'Стек пустрой: {stack.is_empty()}')
#     elif choise == '5':
#         print(f'Стек полный:{stack.is_full()}')
#     elif choise == '6':
#         stack.clrar()
#         print('Стек очищен')
#     elif choise == '7':
#         top_string = stack.top()
#         if top_string:
#             print(f'Значение верхней строки стека: {top_string}')
#         else:
#             print('Стек пуст')
#     elif choise == '0':
#         break
#     else:
#         print('Попробуй ещё, что то не так')
# print('Работа завершена')

# Модуль 14, часть 1, задание 3
# Измените стек из второго задания, таким образом, 
# чтобы его размер был нефиксированным.

class StringStack:

    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print('Стек пуст')
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


stack = StringStack()

while True:
    print('1. Поместить строку в стек')
    print('2. Вытащить строку из стека')
    print('3. Количество строк в стеке')
    print('4. Проверить пустой ли стек')
    print('5. Очистить стек')
    print('6. Получить значение верхней строки стека')
    print('0. Выход')

    choice = input('Выберите операцию: ')

    if choice == '1':
        string = input('Введите строку: ')
        stack.push(string)

    elif choice == '2':
        popped_string = stack.pop()
        if popped_string is not None:
            print(f'Извлеченная строка: {popped_string}')

    elif choice == '3':
        print(f'Количество строк в стеке: {stack.count()}')

    elif choice == '4':
        print(f'Стек пустой: {stack.is_empty()}')

    elif choice == '5':
        stack.clear()
        print('Стек очищен')

    elif choice == '6':
        top_string = stack.top()
        if top_string is not None:
            print(f'Значение верхней строки стека: {top_string}')
        else:
            print('Стек пуст')

    elif choice == '0':
        break

    else:
        print('Попробуйте еще, что-то не так')

print('Работа завершена')
