import math
import sys


class CoefficientReader:
  """Класс для чтения и валидации коэффициентов."""

  @staticmethod
  def get(prompt, arg_val=None):
    if arg_val is not None:
      try:
        return float(arg_val)
      except ValueError:
        print(f"Параметр командной строки '{arg_val}' некорректен.")
    while True:
      try:
        return float(input(f"Введите коэффициент {prompt}: "))
      except ValueError:
        print("Ошибка ввода. Введите действительное число.")


class BiquadraticEquation:
  """Класс для представления и решения биквадратного уравнения."""

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.roots = []

  def solve(self):
    if self.a == 0:
      y_roots = self._solve_linear_or_constant()
    else:
      d = self.b**2 - 4 * self.a * self.c
      if d < 0:
        y_roots = []
      elif d == 0:
        y_roots = [-self.b / (2 * self.a)]
      else:
        sqrt_d = math.sqrt(d)
        y_roots = [
            (-self.b + sqrt_d) / (2 * self.a),
            (-self.b - sqrt_d) / (2 * self.a),
        ]

    if y_roots == "inf":
      self.roots = "inf"
      return

    x_set = set()
    for y in y_roots:
      if y > 0:
        sy = math.sqrt(y)
        x_set.add(sy)
        x_set.add(-sy)
      elif y == 0:
        x_set.add(0.0)
    self.roots = sorted(list(x_set))

  def _solve_linear_or_constant(self):
    if self.b == 0:
      return "inf" if self.c == 0 else []
    return [-self.c / self.b]

  def display_result(self):
    print(f"\nУравнение: ({self.a})*x^4 + ({self.b})*x^2 + ({self.c}) = 0")
    if self.roots == "inf":
      print("Решением является любое действительное число.")
    elif not self.roots:
      print("Действительных корней нет.")
    else:
      print("Корни уравнения:", ", ".join(map(str, self.roots)))


def main():
  args = sys.argv[1:]
  a = CoefficientReader.get("A", args[0] if len(args) > 0 else None)
  b = CoefficientReader.get("B", args[1] if len(args) > 1 else None)
  c = CoefficientReader.get("C", args[2] if len(args) > 2 else None)

  eq = BiquadraticEquation(a, b, c)
  eq.solve()
  eq.display_result()


if __name__ == "__main__":
  main()
