# Day 2

# Study Time: 13 min
# Coding Time: 47 min

# Topic:
# - Conditionals

# Programs:
# - Odd/Even Checker
# - Voting Eligibility Checker
# - Largest of Three Numbers
# - Grade Calculator
# - Leap Year Checker

# Result:
# Task 2 Completed ✔

# Reflection:
# Wrote all programs myself.
# Need to improve speed and confidence.

#Odd/Even
num = int(input("Enter the Number:"))
if num%2 == 0 :
    print(f" {num} is Even ")

else:
    print(f" {num} is Odd")



# Voting Eligibility Checker

Age = int(input(" Enter your Age : "))
if Age >= 18 :
    print("Your are Eligible for Voting")

else:
    print(" you must be 18 years old or older to be eligible for Voting")


# Largest of three numbers

a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))
if a > b and a > c :
    print(f"1st number {a} is the Largest Number")

elif b > a and b > c :
    print(f"2nd number {b} is the Largest Number")

else:
    print(f"3rd number {c} is the Largest Number")

# Grade  Calculator 

Mark = int(input("Enter your Marks (/100): "))
if Mark > 100 or Mark < 0 :
    print("just tell me the actual marks already ")

elif Mark >= 90 :
    print("You got A Grade")

elif Mark >= 80 :
    print("You got B Grade")

elif Mark >= 70 :
    print("You got C Grade")

elif Mark >= 60:
    print("You got  D Grade")
    
elif Mark >= 30:
    print("You are just PASS")

else:
    print("You Failed!!")


# Leap year Checker
# shorter version
# [if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):]
      

year = int(input("Enter the Year : "))

if year%100== 0 and year%4 == 0:
      if year%400 == 0 :
               print(f"{year} is a Leap Year")

      else:
            print(f"{year} is not Leap Year")     
    

elif year%4 == 0 or year%400 == 0 :
    print(f"{year} is a Leap Year")

else:
    print(f"{year} is not Leap Year")

