from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат."""

    _figure_type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls._figure_type

    def __init__(self, side, color_name):
        super().__init__(side, side, color_name)

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Сторона: {}, Площадь: {}".format(
            self.get_figure_type(),
            self.fc.color,
            self.width, # у квадрата ширина равна высоте (сторона)
            self.square()
        )
