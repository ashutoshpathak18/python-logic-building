# # print numbers from 1 to n

n = int(input("Enter the value of n :"))
for i in range(1,n+1):
    print(f"{i}\n")


# # print all even numbers from 1 to 50

for i in range(1,51):
    if i%2 == 0:
        print(i)

# # Take a number n from the user and calculate the sum of numbers from 1 to n.

n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)


# # Take n and reduce it unit 1

n = int(input("Enter the value of n: "))
for i in range(0,n):
    print(n-i)

# using while
while(n!=1):
    n=n-1
    print(n) 

# # Count digit of a number

num = int(input("Enter a number :"))
length = 0
if num == 0:
    length = 1
else:
 while num>0:
    num = num//10
    length+=1

print(length)


# # program to find factorial 

num = int(input("Enter the number :"))
fact = 1
while num > 0:
   fact=fact*num
   num-=1
print(fact)


# reverse a number

num = int(input("Enter a number :"))
rev_num = 0
while(num>0):
    digit = num%10
    rev_num = rev_num*10 + digit
    num = num//10
print(rev_num)


# Determine prime number

num = int(input("Enter a number :"))

for i in range(2,num+1):
    if num%i==0:
        break
if i == num:
    print("prime")
else:
    print("not prime")



# fibonacci series

n = int(input("enter the value of n :"))
num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(0,n):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3


