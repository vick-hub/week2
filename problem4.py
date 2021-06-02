import os
import sys
import math


def calculate(a, b, c):
    x1 = (2 * c) / (-b + math.sqrt(b ** 2 - 4 * a * c))
    x2 = (2 * c) / (-b + math.sqrt(b ** 2 - 4 * a * c))
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1 = {x1}, x2 = {x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())