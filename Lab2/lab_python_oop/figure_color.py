class FigureColor:
    """Класс для хранения и управления цветом фигуры."""
    def __init__(self, color=None):
        self._color = color

    @property
    def color(self):
        """Геттер для получения цвета."""
        return self._color

    @color.setter
    def color(self, value):
        """Сеттер для изменения цвета."""
        self._color = value
