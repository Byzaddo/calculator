import math # imported library for function
import tkinter as tk
import time
import difflib
#===============
# Sub-Programs
#===============

class ShapeCalculator:
    def __init__(self, shape_list):
        self.shape_list = shape_list

    def suggest_shape(self, input_shape):
        suggestions = difflib.get_close_matches(input_shape, self.shape_list, n=3, cutoff=0.8)
        return suggestions

shape_list = ["circle", "square", "rectangle", "triangle", "pentagon", "hexagon", "octagon", "trapezium", "parallelogram"]

calculator = ShapeCalculator(shape_list)

def add(x, y):
    return x + y


def sqrt(x):
    return math.sqrt(x)


def factorial(n):
    if n == 0:
        return 1                #RECURSIVE FUNCTION !!!
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

def log10(x):
    return math.log10(x)

def loge(x):
    return math.log(x)

def log2(x):
    return math.log2(x)


def crcArea(x):
    return math.pi * (x**2)


#trig stuff

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


def sind(x):
    return math.sin(math.radians(x))

def cosd(x):
    return math.cos(math.radians(x))

def tand(x):
    return math.tan(math.radians(x))

def tanadj(opposite, tan_deg):
    adjacentt = opposite / tand(tan_deg)
    return adjacentt

def cosadj(hypotenuse, cos_deg):
    adjacentc = cosd(cos_deg) * hypotenuse
    return adjacentc



#derivatives of trig functions
def dsind(x):
    return cosd(x)

def dcosd(x):
    return -sind(x)

def dtand(x):
    return 1/cosd(x)**2




#Constants

pi = math.pi

tau = math.tau

e = math.e

sqrt2 = "square root of 2, approx 1.41421356237309504880168872420969807856967187537694807317667973799"

#pythogrean theorem a**2 + b**2 = c**2

def findhyp(x, y):
    csqrt = (x**2) + (y**2)
    c = sqrt(csqrt)
    return c

def findadj(a, c):
    bsqrt = (c**2) - (a**2)
    b = sqrt(bsqrt)
    return b

def findopp(b, c):
    asqrt = (c**2) - (b**2)
    a = sqrt(asqrt)
    return a 



print("------ Lord Farquaadulator ------")

#===============
# Main-Program
#===============
delay = True
while True: # loop created for next calculations

    

    if delay:
        print("Select operation.")
        time.sleep(1)
        print("1.Add")
        time.sleep(1)
        print("2.Subtract")
        time.sleep(1)
        print("3.Multiply")
        time.sleep(1)
        print("4.Divide")
        time.sleep(1)
        print("5.Factorial")
        time.sleep(1)
        print("6.Square Root")
        time.sleep(1)
        print("7.Power")
        time.sleep(1)
        print("8.Sine Values (degrees)")
        time.sleep(1)
        print("9.Cos Values (degrees)")
        time.sleep(1)
        print("10.Tan Values (degrees)")
        time.sleep(1)
        print("11.Absolute Value")
        time.sleep(1)
        print("12.logarithm value")
        time.sleep(1)
        print("13.constants")
        time.sleep(1)
        print("14.calculate Area of Circle")
        time.sleep(1)
        print("15.Find the hypotenuse")
        time.sleep(1)
        print("16.Find the adjacent")
        time.sleep(1)
        print("17. Find the opposite")
        time.sleep(1)
        print("18.Area of a shape")
        time.sleep(1)
        print("19.Natural Logarithm value")
        time.sleep(2)


    else:
        
        print("Select operation.")
       
        print("1.Add")
      
        print("2.Subtract")
        
        print("3.Multiply")
        
        print("4.Divide")
       
        print("5.Factorial")
       
        print("6.Square Root")
      
        print("7.Power")
     
        print("8.Sine Values (degrees)")
        
        print("9.Cos Values (degrees)")
        
        print("10.Tan Values (degrees)")
        
        print("11.Absolute Value")
        
        print("12.logarithm value")
        
        print("13.constants")
        
        print("14.calculate Area of Circle")
        
        print("15.Find the hypotenuse")
        
        print("16.Find the adjacent")
        
        print("17. Find the opposite")

        print("18.Area of a shape")

        print("19.Natural Logarithm value")
        
    

    

        
        

    # ===============
    # Selection
    # ===============
    


    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19): ")

    if choice == '7':
        try:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            result = pow(base, exponent)
            print("Answer =", result)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '13':
        try:
            print("pi =", pi)
            print("tau =", tau)
            print("e =", e)
            print("square root of 2 =", sqrt2)
        except ValueError:
            print("invalid input, please enter a number")

    elif choice == '14':
        try:
         r = float(input(("enter the radius of the circle> ")))
         print("the area of the circle is,", crcArea(r))
        except ValueError:
            print("invalid input. please enter a number")

    elif choice == '18':
        try:
            shape = input("Enter the 2D shape you want the area of (square/rectangle/triangle/trapezium/parallelogram): ")
            corrected_shape = shape.lower()
            if corrected_shape not in shape_list:
                suggestions = calculator.suggest_shape(corrected_shape)
                if suggestions:
                    print(f"Did you mean one of these shapes? {', '.join(suggestions)}")
                    user_choice = input("Type 'yes' to use the suggested shape, or anything else to try again: ").lower()
                    if user_choice == 'yes':
                        corrected_shape = suggestions[0]
            if corrected_shape == 'square':
                side_length = float(input("Enter the side length of the square: "))
                print("The area of the square is", side_length ** 2)
            elif corrected_shape == 'rectangle':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                print("The area of the rectangle is", length * width)
            elif corrected_shape == 'triangle':
                base = float(input("Enter the base length of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                print("The area of the triangle is", 0.5 * base * height)
            elif corrected_shape == 'trapezium':
                top_length = float(input("Enter the top side length of the trapezium: "))
                bottom_length = float(input("Enter the bottom side length of the trapezium: "))
                height_trap = float(input("Enter the height of the trapezium: "))
                area_trap = 0.5 * (top_length + bottom_length) * height_trap
                print(f"The area of the trapezium is {area_trap}")
            elif corrected_shape == 'parallelogram':
                side_length = float(input("Enter the length of one side of the parallelogram: "))
                height_para = float(input("Enter the height of the parallelogram: "))
                print("The area of the parallelogram is", side_length * height_para)
            else:
                raise ValueError('Invalid Shape')
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '12':
         try:
          base = input("Enter the base (10/e/2): ")
          xValue = float(input("Enter the value to calculate logarithm: "))
          if base == '10':
              print("The answer is", log10(xValue))
          elif base == 'e':
              print("The answer is", loge(xValue))
          elif base == '2':
              print("The answer is", log2(xValue))
          else:
              print("Invalid base. Please enter '10', 'e', or '2'.")
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

    elif choice in ('15', '16', '17'):
        try:
            if choice == '15':
                a = float(input("enter the length of adjacent side "))
                b = float(input("enter the length of the opposite side "))
                print("the length of the hypotenuse is", findhyp(a, b))
            elif choice == '16':
                b = float(input("enter the length of the opposite side "))
                c = float(input("enter the length of hypotenuse side"))
                print("the length of the adjacent side is", findadj(b, c))
            elif choice == '17':
                a = float(input("enter the length of the adjacent side"))
                c = float(input("enter the length of the hypotenuse"))
                print("the length of the opposite side is ", findopp(a, c))
        except ValueError:
            print("Invalid input. please enter a number")
    
    elif choice in ('8', '9', '10', '11' ):
        try:
            if choice == '8':
             sineNumber = float(input("enter the number you want the sine value of >"))
             print("sine value of", sineNumber, "is", sind(sineNumber))
            elif choice == '9':
                cosNumber = float(input("enter the number you want the cos value of > "))
                print("cosine value of", cosNumber, "is", cosd(cosNumber))
            elif choice == '10':
                tanNumber = float(input("enter the number you want the tan value of >"))
                print("Lord Farquaad says the tan value of", tanNumber, "is", tand(tanNumber))
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
    elif next_calculation.lower() == "yes":
        delay = False
        continue





        #inspired by the Shrekulator




        
  