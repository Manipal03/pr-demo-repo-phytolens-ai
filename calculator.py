"""A tiny calculator. Run it with:  python calculator.py"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


# TODO (issue #1): multiply() is missing. Add it.


def main():
    print("add(4, 3)      =", add(4, 3))
    print("subtract(4, 3) =", subtract(4, 3))
    print("multiply(4, 3) =", multiply(4, 3))


if __name__ == "__main__":
    main()
