from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    """Абстрактный класс геометрической фигуры."""

    @abstractmethod
    def square(self):
        """Абстрактный метод для вычисления площади фигуры."""
        pass
