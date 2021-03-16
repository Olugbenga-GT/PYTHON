from Functions.util import add, multiply

def celcius_to_fahrenheit(celcius: float):
    return add(multiply(celcius, 1.8), 32)

def main():
    temp_c = float(input("input temperature in celcius:    "))
    print("Your temperature in Fahrenheit is ",celcius_to_fahrenheit(temp_c))

if __name__ == "__main__":
    main()


