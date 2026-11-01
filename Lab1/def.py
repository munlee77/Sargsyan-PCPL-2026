import math
import sys


def get_coefficient(prompt, arg_val=None):
  """Функция безопасного ввода коэффициента с поддержкой командной строки."""
  if arg_val is not None:
    try:
      return float(arg_val)
    except ValueError:
      print(
          f"Параметр командной строки '{arg_val}' некорректен. Введите с"
          " клавиатуры."
      )
  while True:
    try:
      return float(input(f"Введите коэффициент {prompt}: "))
    except ValueError:
      print(
          "Ошибка! Некорректный ввод. Требуется ввести действительное число."
      )


def solve_quadratic(a, b, c):
  """Решает квадратное уравнение a*y^2 + b*y + c = 0."""
  if a == 0:
    if b == 0:
      return "inf" if c == 0 else []
    return [-c / b]

  d = b**2 - 4 * a * c
  if d < 0:
    return []
  elif d == 0:
    return [-b / (2 * a)]
  else:
    sqrt_d = math.sqrt(d)
    return [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]


def solve_biquadratic(a, b, c):
  """Решает биквадратное уравнение a*x^4 + b*x^2 + c = 0."""
  y_roots = solve_quadratic(a, b, c)

  if y_roots == "inf":
    return "inf"

  x_roots = set()
  for y in y_roots:
    if y > 0:
      sqrt_y = math.sqrt(y)
      x_roots.add(sqrt_y)
      x_roots.add(-sqrt_y)
    elif y == 0:
      x_roots.add(0.0)

  return sorted(list(x_roots))


def main():
  args = sys.argv[1:]
  a = get_coefficient("A", args[0] if len(args) > 0 else None)
  b = get_coefficient("B", args[1] if len(args) > 1 else None)
  c = get_coefficient("C", args[2] if len(args) > 2 else None)

  print(f"\nУравнение: ({a})*x^4 + ({b})*x^2 + ({c}) = 0")
  roots = solve_biquadratic(a, b, c)

  if roots == "inf":
    print("Решением является любое действительное число.")
  elif not roots:
    print("Действительных корней нет.")
  else:
    print("Корни уравнения:", ", ".join(map(str, roots)))


if __name__ == "__main__":
  main()
