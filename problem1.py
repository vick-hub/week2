import os
import sys


def main():
    name = input("name: ")
    age = int(input("age: "))
    yr_current = int(input("Current year: "))
    born = yr_current - age
    yr_to_77 = 77 - age
    yr_77 = yr_current + yr_to_77
    print(f"The man is called {name} and he is {age} years old.")
    print(f"His year of birth is {born} and he will be 77 in year {yr_77}.")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
