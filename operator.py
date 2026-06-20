
#Create three variables: one integer, one float, and one string. Print the value and type of each using type().


# var1 = 44

# var2 = 23.22

# var3 = "24"

# print("value 1 is", type(var1),var1, "value 2 is", type(var2), var2, "value 3 is", type(var3), var3)


# #urinary operators
# # Equivalent of b = a++ (post-increment)
# a = 10
# b = a
# a += 1

# # Equivalent of b = ++a (pre-increment)
# a += 1
# b = a









"""
********************************************************************************************************************************************************
*/**********************************************************************************************************************************************
*********************************************************************************************************************************************
"""
# 3. Operators
# Easy


# Create calculator for +, -, *, /.


# a = 2
# b = 4

# operator = input("enter operator:>   ")

# if operator == "+":
#     print(a+b)

# elif operator == "-":
#     print(a-b)

# elif operator == "*":
#     print(a*b)
    
# elif operator == "/":
#     print(a/b)




# Find square and cube of number.

# a = 2

# b = 2

# c = 3

# print(a**b)

# print(a**c)








# Find remainder using modulus.

# a= 7
# print(a%2)







# Check whether number is even or odd.


# a = 1

# if a%2==0:
#     print("even")
# else:
#     print("odd")






# Compare two numbers.


# a = 1

# b = 2
# if a>b:
#     print("a is bigger then b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("a is smaller then b")








# Medium



# Find greatest among 3 numbers.

# a = 2
# b = 4
# c = 6

# print("Greatest number is:", max(a, b, c))





# Check if number lies between 1 and 100.

# a = 52

# if 1 <= a <= 100:
#     print("Number lies between 1 and 100")

# else:
#     print("Number does not lie between 1 and 100")







# Create grading system.


# total_marks = 90

# if total_marks >= 90:
#     print("A grade")

# elif total_marks >= 70:
#     print("B grade")

# elif total_marks >= 50:
#     print("C grade")

# else:
#     print("D grade")



# Create age eligibility checker.


# age = 17

# if age < 18:
#     print("cannot vote")

# else:
#     print("can vote")




# Check leap year.


# year = 2024

# if year % 4 == 0:
#     print("Leap year")

# else:
#     print("Not leap year")





# Hard


# Build scientific calculator basics.

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# operator = input("Enter operator: ")

# if operator == "+":
#     print(a + b)

# elif operator == "-":
#     print(a - b)

# elif operator == "*":
#     print(a * b)

# elif operator == "/":

#     if b == 0:
#         print("Cannot divide by zero")

#     else:
#         print(a / b)

# elif operator == "**":
#     print(a ** b)

# elif operator == "%":
#     print(a % b)

# else:
#     print("Invalid operator")







# Create electricity bill calculator.

# units  = 50

# total_cost = 0

# if units <=100:
#     total_cost+=5*units
#     print(f"total cost is: Rs.{total_cost}")

# elif 101 <= units <=200:
#     total_cost+=8*units
#     print(f"total cost is: Rs.{total_cost}")












# Create EMI calculator.

# loan_amount = 500000

# interest_rate = 12 / 100

# months = 6

# time = months / 12

# interest = loan_amount * interest_rate * time

# total_amount = loan_amount + interest

# EMI = total_amount / months

# print("Monthly EMI is:", EMI)







# Create BMI category checker.



# weight = float(input("Enter weight in kg: "))

# height = float(input("Enter height in meters: "))

# height_square = height ** 2

# BMI = weight / height_square

# print("Your BMI is:", BMI)

# if BMI < 18.5:
#     print("Underweight")

# elif BMI <= 24.9:
#     print("Normal")

# else:
#     print("Overweight")







# Build marks comparison system for students.




# student_marks = {
#     "pratham": 85,
#     "salman": 92,
#     "vijay": 78
# }

# print(max(student_marks.values()))












