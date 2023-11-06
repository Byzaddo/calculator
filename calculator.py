import math # imported library for function

import tkinter 
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

def abs(x):
    return math.fabs(x)


#trig stuff

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))


def sind(x):
    return math.sin(math.degrees(x))

def cosd(x):
    return math.cos(math.degrees(x))

def tand(x):
    return math.tan(math.degrees(x))






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
    print("8.Sine Values (Radians)")
    print("9.Cos Values (radians)")
    print("10.Tan Values (radians)")
    print("11.Absolute Value")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")

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
    
    elif choice in ('8', '9', '10', '11' ):
        try:
            if choice == '8':
             sineNumber = float(input("enter the number you want the sine value of >"))
             print("sine value of", sineNumber, "is", sin(sineNumber))
            elif choice == '9':
                cosNumber = float(input("enter the number you want the cos value of > "))
                print("cosine value of", cosNumber, "is", cos(cosNumber))
            elif choice == '10':
                tanNumber = float(input("enter the number you want the tan value of >"))
                print("The tan value of", tanNumber, "is", tan(tanNumber))
            elif choice == '11':
                absolVal = float(input("enter the number you want the absolutr value of >"))
                print("the absolute value of", absolVal, "is", abs(absolVal))
        except ValueError:
            print("Invalid input, please enter a number")


    else:
        print("invalid input.")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ") # Ask next calculation
    if next_calculation.lower() == "no":
        break # if answer no end the program

