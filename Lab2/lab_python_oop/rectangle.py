from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Rectangle(GeometricFigure):
    """Класс Прямоугольник."""

    _figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls._figure_type

    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.fc = FigureColor(color_name)

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Ширина: {}, Высота: {}, Площадь: {}".format(
            self.get_figure_type(),
            self.fc.color,
            self.width,
            self.height,
            self.square()
        )
