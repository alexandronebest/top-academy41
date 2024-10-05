# Модуль 10, задание 1
# Создать базовый класс Фигура с методом для подсчета 
# площади. Создать производные классы: прямоугольник, 
# круг, прямоугольный треугольник, трапеция со своими 
# методами для подсчета площади. 


# class Figure:
#     def __init__(self, name: str):
#         self._name:str = Figure._validate_name(name)

#     @staticmethod
#     def _validate_name(name: str) -> str:
#         if name.isalpha():
#             return name
#         raise Exception('Имя должно содержать только буквы')
    
#     def __str__(self) -> str:
#         return f'{self._name}'
    

# class Rectangle(Figure):
#     def __init__(self, name: str, height: int, width: int):
#         super().__init__(name)
#         self.height = height
#         self.width = width

#     def square_rectangle(self) -> int:
#         return self.height * self.width

#     def __str__(self) -> str:
#         return f'1) Прямоугольник, высотой:{self.height}, длинной: {self.width}, площадью {self.square_rectangle()} см2'


# class Circle(Figure):
#     def __init__(self, name: str, radius: int):
#         super().__init__(name)
#         self.radius = radius

#     def square_circle(self) -> int:
#         return 3.14 * (self.radius * self.radius)

#     def __str__(self) -> str:
#         return f'2) Круг, радиусом: {self.radius}, плащадь равна: {self.square_circle()} см2'


# class Right_triangle(Figure):
#     def __init__(self, name: str, leg1: int, leg2: int):
#         super().__init__(name)
#         self.leg1 = leg1
#         self.leg2 = leg2

#     def square_right_triangle(self) -> int:
#         return self.leg1 * self.leg2 / 2

#     def __str__(self) -> str:
#         return f'3) Прямоугольный треугольник, с катетом 1 = {self.leg1}, катетом 2 = {self.leg2}, плащадь равна: {self.square_right_triangle()} см2'


# class Trapezoid(Figure):
#     def __init__(self, name: str, trapezoid_length1: int, trapezoid_length2: int, trapezoid_height: int):
#         super().__init__(name)
#         self.trapezoid_length1 = trapezoid_length1
#         self.trapezoid_length2 = trapezoid_length2
#         self.trapezoid_height = trapezoid_height

#     def square_rectangle(self) -> int:
#         return (self.trapezoid_length1 + self.trapezoid_length2) * self.trapezoid_height

#     def __str__(self) -> str:
#         return f'4) Трапеция, с первой длинной: {self.trapezoid_length1} и со второй длинной: {self.trapezoid_length2} и высотой трапеции: {self.trapezoid_height}, площадь равна: {self.square_rectangle()} см2'


# f1 = Rectangle('прямоугольник', 5, 10)
# print(f1)
# f2 = Circle('Круг', 10)
# print(f2)
# f3 = Right_triangle('Прямоугольныйтреугольник', 10, 15)
# print(f3)
# f4 = Trapezoid('Трапеция', 10, 12, 6)
# print(f4)


# # Модуль 10, задание 2
# # Для классов из задания 1 нужно переопределить магические методы 
# # int(возвращает площадь) и str(возвращает 
# # информацию о фигуре).


class Figure:
    def __init__(self, name: str):
        self._name:str = Figure._validate_name(name)

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return name
        raise Exception('Имя должно содержать только буквы')
    
    def __str__(self) -> str:
        return f'{self._name}'
    

class Rectangle(Figure):
    def __init__(self, name: str, height: int, width: int):
        super().__init__(name)
        self.height = height
        self.width = width

    def square_rectangle(self) -> int:
        return self.height * self.width
    
    def __int__(self) -> float:
        return int(self.square_rectangle())

    def __str__(self) -> str:
        return f'1) Прямоугольник, высотой:{self.height}, длинной: {self.width}'


class Circle(Figure):
    def __init__(self, name: str, radius: int):
        super().__init__(name)
        self.radius = radius

    def square_circle(self) -> float:
        return 3.14 * (self.radius * self.radius)

    def __int__(self) -> int:
        return int(self.square_circle())

    def __str__(self) -> str:
        return f'2) Круг, радиусом: {self.radius}'


class Right_triangle(Figure):
    def __init__(self, name: str, leg1: int, leg2: int):
        super().__init__(name)
        self.leg1 = leg1
        self.leg2 = leg2

    def square_right_triangle(self) -> int:
        return self.leg1 * self.leg2 / 2

    def __int__(self) -> float:
        return int(self.square_right_triangle())

    def __str__(self) -> str:
        return f'3) Прямоугольный треугольник, с катетом 1 = {self.leg1}, катетом 2 = {self.leg2}'

class Trapezoid(Figure):
    def __init__(self, name: str, trapezoid_length1: int, trapezoid_length2: int, trapezoid_height: int):
        super().__init__(name)
        self.trapezoid_length1 = trapezoid_length1
        self.trapezoid_length2 = trapezoid_length2
        self.trapezoid_height = trapezoid_height

    def square_Trapezoid(self) -> int:
        return (self.trapezoid_length1 + self.trapezoid_length2) * self.trapezoid_height

    def __int__(self) -> float:
        return int(self.square_Trapezoid())

    def __str__(self) -> str:
        return f'4) Трапеция, с первой длинной: {self.trapezoid_length1} и со второй длинной: {self.trapezoid_length2} и высотой трапеции: {self.trapezoid_height}'

Figura1 = Rectangle('прямоугольник', 5, 10)
print(Figura1)
print(int(Figura1))  # Площадь прямоугольника

Figura2 = Circle('Круг', 10)
print(Figura2)
print(int(Figura2))

Figura3 = Right_triangle('Прямоугольныйтреугольник', 10, 15)
print(Figura3)
print(int(Figura3))

Figura4 = Trapezoid('Трапеция', 10, 12, 6)
print(Figura4)
print(int(Figura4))


