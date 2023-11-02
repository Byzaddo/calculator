import math # imported library for function

#===============
# Sub-Programs
#===============


def add(x, y):
    return x + y


def sqrt(x):
    return math.sqrt(x)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y





#===============
# Main-Program
#===============

while True: # loop created for next calculations

    # ===============
    # Selection
    # ===============

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Factorial")
    print("6.Square Root")
    print("7.Power")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        try:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            result = pow(base, exponent)
            print("Answer =", result)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice in ('5', '6'):
        try:
            num3 = int(input("Enter the number you want to calculate: "))
            if choice == '5':
                print(num3, "factorial is", factorial(num3))
            elif choice == '6':
                print("Square root of", num3, "is", sqrt(num3))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print("invalid input.")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ") # Ask next calculation
    if next_calculation.lower() == "no":
        break # if answer no end the program

