# A variable is simply a name that refers to a value.

a = 15  # Here a is variable 
print("/n",a)

# Program to calculate area of rectangle

lenght = eval(input("Enter the length of the rectangle in meter:"))
width = eval(input("Enter the width of the rectangle in meter:"))
area = lenght * width
if lenght == width:
    print("It is a Square...! ")
    print(f"Area of the square is {area} sq. meter\n")
else:
    print(f"Area of the rectangle is {area} sq. meter\n")

# Here length width and area are the variables.


# Swapping two numbers using third variable

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

print("Before swapping.......")
print(f"a = {a}\nb = {b}")

print("after swapping........")
c = a
a = b
b = c
print(f"a = {a}\nb = {b}")