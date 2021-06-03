import os
import sys
import math


def calculate(a, b, c,):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    x1 = (2 * c) / (-b + math.sqrt(discriminant))
    x2 = (2 * c) / (-b - math.sqrt(discriminant))
    return x1, x2


def main():
    a, b, c = map(float, input("please enter the coefficients: ").split(",", 2))
    x1, x2 = calculate(a, b, c)
    print(f"x1 = {x1}, x2 = {x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
