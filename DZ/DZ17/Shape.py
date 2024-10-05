# Модуль 10, задание 3
# Создайте базовый класс Shape для рисования плоских 
# фигур. 
# Определите методы: 

# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.

# Определите производные классы: 
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего 
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами 
# этого прямоугольника.

# Создайте список фигур, сохраните фигуры в файл, 
# загрузите в другой список и отобразите информацию о 
# каждой из фигур.


from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type: str):
        self.shape_type = shape_type

    @abstractmethod
    def show(self):
        pass

    def save(self):
        with open('shapes.txt', 'a', encoding='utf-8') as f:
            f.write(self.__str__() + '\n')

    @staticmethod
    def load():
        with open('shapes.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]

class Square(Shape):
    def __init__(self, coordinate_x: int, coordinate_y: int, side_one: int):
        super().__init__('Square')
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.side_one = side_one

    def show(self):
        return f'Фигура: {self.shape_type}, с координатами: ({self.coordinate_x}, {self.coordinate_y}), сторона: {self.side_one}'

    def __str__(self):
        return self.show()

class Rectangle(Shape):
    def __init__(self, coordinate_x: int, coordinate_y: int, width: int, height: int):
        super().__init__('Rectangle')
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.width = width
        self.height = height

    def show(self):
        return f'Фигура: {self.shape_type}, с координатами: ({self.coordinate_x}, {self.coordinate_y}), ширина: {self.width}, высота: {self.height}'

    def __str__(self):
        return self.show()

class Circle(Shape):
    def __init__(self, coordinate_x: int, coordinate_y: int, radius: int):
        super().__init__('Circle')
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def show(self):
        return f'Фигура: {self.shape_type}, с координатами: ({self.coordinate_x}, {self.coordinate_y}), радиус: {self.radius}'

    def __str__(self):
        return self.show()

class Ellipse(Shape):
    def __init__(self, coordinate_x: int, coordinate_y: int, width: int, height: int):
        super().__init__('Ellipse')
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.width = width
        self.height = height

    def show(self):
        return f'Фигура: {self.shape_type}, с координатами: ({self.coordinate_x}, {self.coordinate_y}), ширина: {self.width}, высота: {self.height}'

    def __str__(self):
        return self.show()

shapes = [
    Square(1, 2, 5),
    Rectangle(3, 4, 6, 8),
    Circle(5, 5, 3),
    Ellipse(6, 7, 4, 2)
]

for shape in shapes:
    shape.save()

loaded_shapes = Shape.load()

for line in loaded_shapes:
    print(line)