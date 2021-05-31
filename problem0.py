import os
import sys


# def description(name, age):
name = "name"
age = "age"


def main():
    name = input("name: ")
    age = int(input("age: "))
    print(f"The man is called {name} and he is {age} years old.")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
