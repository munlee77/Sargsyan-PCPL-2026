import math
import sys


def get_coefficient(prompt, arg_val=None):
  if arg_val is not None:
    try:
      return float(arg_val)
    except ValueError:
      print(f"Параметр командной строки '{arg_val}' некорректен.")
  while True:
    try:
      return float(input(f"Введите коэффициент {prompt}: "))
    except ValueError:
      print("Ошибка: требуется ввести действительное число.")


def calculate_y_roots(a, b, c):
  d = b**2 - 4 * a * c
  match (a == 0, d > 0, d == 0, d < 0):
    case (True, _, _, _):
      match b == 0:
        case True:
          return "inf" if c == 0 else []
        case False:
          return [-c / b]
    case (_, True, _, _):
      sqrt_d = math.sqrt(d)
      return [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]
    case (_, _, True, _):
      return [-b / (2 * a)]
    case (_, _, _, True):
      return []


def transform_y_to_x(y_roots):
  match y_roots:
    case "inf":
      return "inf"
    case _:
      x_set = set()
      for y in y_roots:
        match (y > 0, y == 0):
          case (True, _):
            sy = math.sqrt(y)
            x_set.update([sy, -sy])
          case (_, True):
            x_set.add(0.0)
          case _:
            pass
      return sorted(list(x_set))


def main():
  args = sys.argv[1:]
  a = get_coefficient("A", args[0] if len(args) > 0 else None)
  b = get_coefficient("B", args[1] if len(args) > 1 else None)
  c = get_coefficient("C", args[2] if len(args) > 2 else None)

  print(f"\nУравнение: ({a})*x^4 + ({b})*x^2 + ({c}) = 0")
  y_roots = calculate_y_roots(a, b, c)
  roots = transform_y_to_x(y_roots)

  match roots:
    case "inf":
      print("Решением является любое действительное число.")
    case []:
      print("Действительных корней нет.")
    case _ as lst:
      print("Корни уравнения:", ", ".join(map(str, lst)))
if __name__ == "__main__":
  main()
