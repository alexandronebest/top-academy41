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

import json

class Shape:
    def __init__(self, type_figure: str):
        self.type_figure = type_figure

    def show(self):
        raise NotImplementedError("Метод show() должен быть переопределён в производном классе.")

    def save(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.__dict__) + '\n')

    @staticmethod
    def load(filename):
        shapes = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                shape_data = json.loads(line.strip())
                shape_type = shape_data.pop("type_figure")
                if shape_type == "Square":
                    shapes.append(Square(**shape_data))
                elif shape_type == "Rectangle":
                    shapes.append(Rectangle(**shape_data))
                elif shape_type == "Circle":
                    shapes.append(Circle(**shape_data))
                elif shape_type == "Ellipse":
                    shapes.append(Ellipse(**shape_data))
        return shapes


class Square(Shape):
    def __init__(self, x: int, y: int, side_length: int):
        super().__init__("Square")
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        return f"Square: Upper Left Corner: ({self.x}, {self.y}), Side Length: {self.side_length}"


class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__("Rectangle")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Rectangle: Upper Left Corner: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}"


class Circle(Shape):
    def __init__(self, center_x: int, center_y: int, radius: int):
        super().__init__("Circle")
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        return f"Circle: Center: ({self.center_x}, {self.center_y}), Radius: {self.radius}"


class Ellipse(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__("Ellipse")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Ellipse: Upper Left Corner: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}"


# Пример
shapes_list = [
    Square(0, 0, 5),
    Rectangle(1, 1, 4, 2),
    Circle(5, 5, 3),
    Ellipse(0, 0, 6, 4)
]

# Сохранение 
for shape in shapes_list:
    shape.save('shapes.txt')

# Загрузка фигур из файла
loaded_shapes = Shape.load('shapes.txt')

# Отображение информации о загруженных
for shape in loaded_shapes:
    print(shape.show())

