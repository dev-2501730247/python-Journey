# Day 1

# Study Time: 32 min
# Coding Time: 50 min

# Topics:
# - Variables
# - Data Types
# - Input
# - Print
# - F-Strings

# Programs:
# - Age Calculator
# - Swap Numbers
# - Basic Calculator

# Reflection:
# Could write most code without looking up syntax.
# Need more practice with confidence.





#variables : reusable containers which act like their values 

name = "Dev Kaushik"
age = 18
clg = "krmu"

# f-string:
print(f"Your Name is {name}")
print(f"Your age is {age}")
print(f"You are std of {clg}")

print("Your Name is", name)


print("Your are "+ str(age) + " year old")


print(input("Enter your name:"))

name = (input("Enter your name:"))
age = int(input("Enter your age:"))
height = float(input("Enter How tall are you  : "))
newage = age + 1
heightiny = height + 1.09

print(name)
print(age)
print(newage)
print(height)
print(heightiny)

# Age Calculator
dob = int(input("Enter your year of your of birth "))
year = int(input("Enter what year is it "))
age  =  year - dob
print(f"your age is {age}")

# swap two number
a = 20
b = 30 
print(a,b)
a,b = b,a
print(a,b)

a,b = b,a= 20 ,30 
print(a,b)

#basic Calculator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = a + b
sub = a - b
product = a * b 
division = a/b
print(f"Sum of these number is {sum}")
print(f"subtraction of these numbers is {sub}")
print(f"Product of these Numbers is {product}")
print(f"Division of these number is {division}")
