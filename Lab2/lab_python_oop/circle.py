import math
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Circle(GeometricFigure):
    """Класс Круг."""

    _figure_type = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls._figure_type

    def __init__(self, radius, color_name):
        self.radius = radius
        self.fc = FigureColor(color_name)

    def square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Радиус: {}, Площадь: {:.2f}".format(
            self.get_figure_type(),
            self.fc.color,
            self.radius,
            self.square()
        )
