
def add(num1: float, num2: float) -> float:
    """ a function that adds two numbers """
    # logic here
    num3 = num1 + num2
    return num3


def subtract(num1: float, num2: float) -> float:
    """ a function that subtracts a number from another """
    # logic here
    num3 = num1 - num2
    return num3


def multiply(num1: float, num2: float) -> float:
    """ a function that adds two numbers """
    # logic here
    num3 = num1 * num2
    return num3


def divide(num1: float, num2: float) -> float:
    """ a function that adds two numbers """
    # logic here
    num3 = num1 / num2
    return num3


def square_root(num1: float) -> float:
    """ a function that adds two numbers """
    # logic here
    num2 = num1 ** 0.5
    return num2


def square(num1: float) -> float:
    """ a function that adds two numbers """
    # logic here
    num2 = num1 ** 2
    return num2


def main():
    # run all the tests
    # run_tests()
    # print("all tests passed")

    # add 2 nums
    x = 2
    y = 10
    z = add(x, y)
    print(f"x + y: {x} + {y} = {z}")


if __name__ == "__main__":
    main()
