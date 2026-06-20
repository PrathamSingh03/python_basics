'''Take a variable n. Print "Even" if the number is even and "Odd" if it's odd. Also print whether it is positive or negative (or zero).

SAMPLE

Input: n = -7
Output: Odd Negative
Input: n = 4
Output: Even Positive
'''

'''
num1= 4

if(num1=="+" and num1%2==0):
    if("num1=="-" and num1%2==0"):
        print("Even Negative")
        if("num1=="+" and num1%2!=0"):
            print("Odd Positive ")
        else:
            print("Odd Negative")
    else:
        print("Odd Negative")

else:
    print("0")
'''

















# age = 19

# if(age>=20):
#     print("voter")

# elif(age>=18):
#     print("just voter")

# else:
#     print("not eligible")


# #odd even


# var1 = 22

# if(var1 %2==0):
#     print("even")

# else:
#     print("odd")








# grade students based on their marks


# mark1 = float(input("what are your marks: "))

# if(mark1>=90):
#     print("A")

# elif(mark1>=80 and mark1<90):
#     print("B")

# elif(mark1>=80 and mark1<70):
#     print("C")

# else:
#     print("D")









# driving_age = int(input("what is your age:  "))

# if(driving_age >= 18):
#     if(driving_age>=80):
#         print("too old")
#     else:
#         print("cann drive")

# else:
#     print("tennager")













#write a program to check the greatest 3 numbers enterred by the user.


# num1= int(input("enter number 1: "))
# num2= int(input("enter number 2: "))
# num3= int(input("enter number 3: "))

# if(num1 > num2 and num1 > num3):
#     print("number 1 is greatest")

# elif(num2 > num1 and num2 > num3):
#     print("number 2 is greatest")

# else:
#     print("number 3 is greatest")













#write a program to check if a number is a mutiple 7 or not.

# num1= 15

# if(num1%7==0):
#     print("is a mutiple of 7")

# else:
#     print("not a multiple")














'''Q1 · Age checker

Take a variable age and print "Minor" if age is below 18, "Adult" if 18–59, and "Senior" if 60 or above.

'''



# age= int(input("enter your age: "))

# if(age<18):
#     print("minor")

# elif(age<=59):
#     print("adult")

# else:
#     print("Old")













'''Q2 · Simple calculator

Take two numbers a = 15 and b = 4. Print their sum, difference, product, quotient (normal division), quotient (floor division), and remainder — each on a separate line with a label.

SAMPLE

Input: a=15, b=4
Output: Sum: 19 Diff: 11 Product: 60 Quotient: 3.75 Floor: 3 Remainder: 3'''


'''
a=float(input("enter 1st number: "))

b=float(input("enter 2nd number: "))

op=input("enter operator: ")

if(op=="+"):
    print(a+b,"addition")

elif(op=="-"):
    print(a-b, "minus")

elif(op=="*"):
    print(a*b, "multiply")

elif(op=="/"):
    print(a*b, "divide")

elif(op=="//"):
    print(a//b, "Quotient")

elif(op=="%"):
    print(a%b, "reminader")

else:
    print("wrong operator")
'''



























'''Q2. Basic calculator
Take two numbers a = 15 and b = 4. Print the result of: addition, subtraction, multiplication, division, floor division, modulo, and exponentiation.'''

'''
num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))



operator = input("Enter operator (+, -, *, /, //, %, **): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    print("Result:", num1 / num2)
elif operator == "//":
    print("Result:", num1 // num2)
elif operator == "%":
    print("Result:", num1 % num2)
elif operator == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operator!")

'''


# Q1
# Easy
# Write if/else to check if n = 7 is positive or negative.
# 💡 Show Hint
# ✅ Show Solution



# n = 7
# if n > 0:
#     print('Positive')
# else:
#     print('Negative')






# Q2
# Easy
# Write if/elif/else for score = 78: A>=90, B>=80, C>=70, else F.
# 💡 Show Hint
# ✅ Show Solution


# score  = 78

# if score >= 90:
#     print("A")

# elif score >=80:
#     print("B")

# elif score >=70:
#     print("C")

# else:
#     print("F")





# Q3
# Easy
# Check if n = 12 is even or odd.
# 💡 Show Hint
# ✅ Show Solution


# n = 12
# if n % 2 == 0:
#     print('Even')
# else:
#     print('Odd')











# Q4
# Easy
# Predict the output:

# if 0:
#     print('yes')
# else:
#     print('no')
# 💡 Show Hint
# ✅ Show Solution

# Output: no










# Q5
# Easy
# Check if x = 5 is between 1 and 10 using a single chained condition.
# 💡 Show Hint
# ✅ Show Solution


# x = 5

# if 1 <= x <= 10:
#     print("between 1-10")








# Q6
# Medium
# Nested if: if age >= 18 check for license. Print 'Can drive', 'No license', 'Too young'.
# 💡 Show Hint
# ✅ Show Solution


# age = int(input("Enter age: "))
# license = input("Have license? (yes/no): ")

# if age >= 18:
#     if license.lower() == "yes":
#         print("Can drive")
#     else:
#         print("No license")
# else:
#     print("Too young")





# Q7
# Medium
# Predict the output:

# x = 5
# if x > 3:
#     if x > 7:
#         print('big')
#     else:
#         print('medium')
# else:
#     print('small')
# 💡 Show Hint
# ✅ Show Solution

# Output: medium






# Q8
# Medium
# Use a ternary expression to assign 'adult' or 'minor' based on age = 20.
# 💡 Show Hint
# ✅ Show Solution


# age = 20
# status = 'adult' if age >= 18 else 'minor'
# print(status)   # adult















# Q9
# Medium
# Predict the output:

# x = 0
# if x or 5 > 3:
#     print('yes')
# else:
#     print('no')
# 💡 Show Hint
# ✅ Show Solution

# Output :Yes




# Q10
# Medium
# Check if lst = [] is empty using 'not'. Print 'empty' or 'has items'.
# 💡 Show Hint
# ✅ Show Solution


# lst = [1]


# if not lst :
#     print("empty")

# else:
#     print("has items")





# Q11
# Hard
# Predict the output:

# if True and False or True:
#     print('yes')
# else:
#     print('no')
# 💡 Show Hint
# ✅ Show Solution

# (True and False) or True = True
# Output: yes








# Q12
# Hard
# Write a chained ternary to print 'A', 'B', or 'C' based on score = 85.
# 💡 Show Hint
# ✅ Show Solution



# score = 85
# grade = "A" if score >= 90 else "B" if score >= 80 else "C"
# print(grade)   # Output: B



# Q13
# Hard
# Write FizzBuzz: 'FizzBuzz' if div by 3 and 5, 'Fizz' if by 3, 'Buzz' if by 5, else the number.
# 💡 Show Hint
# ✅ Show Solution


# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# fizzbuzz(15)   # FizzBuzz
# fizzbuzz(9)    # Fizz
# fizzbuzz(10)   # Buzz
# fizzbuzz(7)    # 7






# Q14
# Hard
# Predict the output:

# x = None
# if x is None:
#     print('nothing')
# elif x == None:
#     print('equal')
# 💡 Show Hint
# ✅ Show Solution

# Output: Nothing





# Q15
# Hard
# Predict the output:
# x = 5
# result = 'big' if x > 10 else 'medium' if x > 3 else 'small'
# print(result)




# Output: medium
