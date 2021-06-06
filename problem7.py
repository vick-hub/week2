import os
import sys
import math


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        # good attempt but incorrect
        # test your answers at https://www.calculatorsoup.com/calculators/algebra/quadratic-formula-calculator.php
        return complex(-b, -discriminant), complex(-b, discriminant)
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f" x1 = {x1}, x2 = {x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
