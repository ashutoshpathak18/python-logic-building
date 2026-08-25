# print numbers from 1 to n

# n = int(input("Enter the value of n :"))
# for i in range(1,n+1):
#     print(f"{i}\n")


# print all even numbers from 1 to 50

# for i in range(1,51):
#     if i%2 == 0:
#         print(i)

# Take a number n from the user and calculate the sum of numbers from 1 to n.

# n = int(input("Enter the value of n: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum+i
# print(sum)


# Take n and reduce it unit 1

# n = int(input("Enter the value of n: "))
# for i in range(0,n):
#     print(n-i)

# using while
# while(n!=1):
#     n=n-1
#     print(n) 

# Count digit of a number

# num = int(input("Enter a number :"))
# length = 0
# if num == 0:
#     length = 1
# else:
#  while num>0:
#     num = num//10
#     length+=1

# print(length)


# program to find factorial 

num = int(input("Enter the number :"))
fact = 1
while num > 0:
   fact=fact*num
   num-=1
print(fact)



