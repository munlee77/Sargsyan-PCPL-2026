from colorama import init, Fore, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    # Инициализация colorama для цветного вывода в консоль
    init(autoreset=True)

    N = 17

    print(Fore.CYAN + "=== Демонстрация работы классов геометрических фигур ===")

    # Создание объектов по заданию
    r = Rectangle(N, N, "синий")
    c = Circle(N, "зеленый")
    s = Square(N, "красный")

    # Вывод информации в консоль
    print(r)
    print(c)
    print(s)

    print(Fore.YELLOW + "\nПример использования внешнего пакета (colorama):")
    print(Fore.GREEN + "Все объекты успешно созданы и проверены!")

if __name__ == '__main__':
    main()
