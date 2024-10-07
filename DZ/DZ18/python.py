# Модуль 10, задание 1
# Создайте функцию, возвращающую список со всеми 
# простыми числами от 0 до 1000. 
# Используя механизм декораторов посчитайте сколько 
# секунд, потребовалось для вычисления всех простых чисел. 
# Отобразите на экран количество секунд и простые числа.]

# from time import time

# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = func(*args, **kwargs)
#         end_time = time()
#         print('Время заняло: {:.3f} секунд'.format(end_time - start_time))
#         return result
#     return wrapper

# @time_decorator
# def simple_numb(n):
#     prime_numbers = []
#     for i in range(2, n + 1):
#         if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
#             prime_numbers.append(i)
#     return prime_numbers

# prime_numbers = simple_numb(1000)
# print('Простые числа:', prime_numbers)

# Модуль 10, задание 2 
# Добавьте к первому заданию возможность передавать 
# границы диапазона для поиска всех простых чисел.

from time import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print('Время заняло: {:.3f} секунд'.format(end_time - start_time))
        return result
    return wrapper

@time_decorator
def simple_numb(lower, upper):
    prime_numbers = []
    for i in range(lower, upper + 1):
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            prime_numbers.append(i)
    return prime_numbers

lower_bound = 0
upper_bound = 1000
prime_numbers = simple_numb(lower_bound, upper_bound)
print('Простые числа в диапазоне от {} до {}: {}'.format(lower_bound, upper_bound, prime_numbers))

# Модуль 10, задание 3 
# Каждый год ваша компания предоставляет различным 
# государственным организациям финансовую отчетность. 
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос 
# отчетности для организаций.

def log_method_call(method):
    """Декоратор для логирования вызовов методов."""
    def wrapper(*args, **kwargs):
        result = method(*args, **kwargs)
        print(f'Вызван метод {method.__name__} с аргументами {args[1:]} и результатом {result}')
        return result
    return wrapper

class Organization:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

class VTB_bank(Organization):
    def __init__(self, name: str, profit: int):
        self.name = name  
        self.profit = profit

    def __str__(self) -> str:
        return f'{self.name}: Прибыль: {self.profit}'

    @log_method_call
    def clean_profit(self):
        return self.profit - (self.profit / 100 * 13)

    @log_method_call
    def __int__(self) -> int:
        return int(self.clean_profit())
    
class T_bank(Organization):
    def __init__(self, name: str, profit: int):
        self.name = name  
        self.profit = profit

    def __str__(self) -> str:
        return f'{self.name}: Прибыль: {self.profit}'

    @log_method_call
    def clean_profit(self):
        return self.profit - (self.profit / 100 * 13)

    @log_method_call
    def __int__(self) -> int:
        return int(self.clean_profit())
    

res = VTB_bank('VTB', 150000000)
print(res)  
print(int(res)) 

res2 = T_bank('T', 250000000)
print(res2)  
print(int(res2)) 

        