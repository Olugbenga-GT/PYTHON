from calculator import *

def run_tests():
    """ test all the functions """
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert subtract(3, 2) == 1, "3 - 2 is 1"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert divide(6, 2) == 3, "6 / 2 is 3"
    assert square_root(25) == 5, "square root of 25 is 5"
    assert square(6) == 36, "square of 6 is 36"
    print("Hello")


if __name__ == "__main__":
    run_tests()
