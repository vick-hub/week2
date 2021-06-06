import os
import sys
import random


def main():
    t = random.randint(0, 9)
    y = int(input("Enter a number: "))
    # we're to apply what we learned; this has not been introduced
    if y < t:
        print("The number is less than random number")
    else:
        print("The number is not less than random number")
        return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
