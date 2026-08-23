# Program to check voting eligibility

age = int(input("Enter you age :"))
if age >= 18 and age <= 100:
    print("You are eligible to vote")
elif age > 0  and age <18:
    print("You are not eligible kidoo..")
elif age > 100 and age < 110:
    print("you still alive???? you can vote")
else:
    print("Are you ghost...")
print("\n \n")


# program to find larget and smallest of three number using nested loop

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    if b > c:
        print(f"{a} is largest and {c} is smallest ")
    else:
        print(f"{a} is largest and {b} is smallest")
elif b > a and b >c:
    if a > c:
        print(f"{b} is largest and {c} is smallest")
    else:
        print(f"{b} is largest and {a} is smallest")
else:
    if a > b:
        print(f"{c} is largest and {b} is smallest")
    else:
        print(f"{c} is largest and {a} is smallest")



#  Triangler Validator

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a+b > c and b+c >a and c+a > b:
    print("the sides can form a triangle")
else: 
    print("triangle not possible")