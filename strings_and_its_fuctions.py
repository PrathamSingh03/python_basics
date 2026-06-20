

'''
Q3. Convert and compute
You are given num1 = "25" and num2 = "10" as strings. Convert them to integers and print their sum, difference, and product.
'''

# num1 = "25"
# num2 = "10"

# sum=("the result" ,int(num1),int(num2))

# print()






# var1 = "my name is jai"

# var2= (var1.capitalize())

# print(var2)



# var1 = "my name my"

# print(var1.find("y"))




# var1 = "my name my"

# print(var1.count("y"))




# Write a code to input user name and print its length

# var1 = str(input("what is you name"))

# print("your name is: ", var1, "\n" ,len(var1))



# var1 = "what i#s you# name"

# print(var1.count("#"))







'''
Take s = "I hate Mondays and I hate traffic". Replace every occurrence of "hate" with "dislike" and print the result.

SAMPLE

Input:  s = "I hate Mondays and I hate traffic"
Output: I dislike Mondays and I dislike traffic
'''




# s = "I hate Mondays and I hate traffic"

# print(s.replace("hate","dislike"))

'''
Q6 · Reverse a string

Take s = "Hello World". Print the string reversed using slicing.

SAMPLE

Input:  s = "Hello World"
Output: dlroW olleH

'''



# s = input("enter here: ")

# print(f"a: is {s.count('a')}")
# print(f"e: is {s.count('e')}")
# print(f"i: is {s.count('i')}")
# print(f"o: is {s.count('o')}")
# print(f"u: is {s.count('u')}")




'''
Q7 · Find the domain

Take email = "student@gmail.com". Using find() and slicing, extract and print only the domain part — "gmail.com".

'''


# email = "student@gmail.com" 

# find_atrate = email.find("@")

# print(email[find_atrate+1:len(email)])




# (better version) split fuction


# email ="student@gmail.com"

# var1 = email.split("@") 
# print(var1[1])



# email = "student@gmail.com"

# pos = email.find("@")

# if pos != -1:                  # -1 means "@" was not found
#     print(email[pos + 1:])     # slice everything after @
# else:
#     print("Invalid email")




'''Q1 · Extract the username

Take email = "student@gmail.com". Extract and print only the username part — everything before the @.

'''
'''
email = "student@gmail.com"

name = email.find("@")

if name != -1:                 
    print(email[:name - 0])     

else:
    print("Invalid email")
'''
















'''Q2 · Extract after the slash

Take path = "home/documents/file.txt". Find the first '/' and print everything after it.

SAMPLE

Input:  path = "home/documents/file.txt"
Output: documents/file.txt

'''




'''

path = "home/documents/file.txt"

variable1 = path.find("/")

if variable1 != -1:                 
    print(path[variable1 + 1 :])     

else:
    print("Invalid")

'''

# path = "home/documents/file.txt"
# spilt_var = path.split("/")
# print(spilt_var[1:len(path)])









'''Q4 · Extract the filename

Take path = "documents/report.pdf". Extract and print only the filename — "report.pdf" — which comes after the '/'.

SAMPLE

Input:  path = "documents/report.pdf"
Output: report.pdf
Input:  path = "downloads/photo.jpg"
Output: photo.jpg

'''

# path = "documents/report.pdf"

# split_var = path.split("/")

# print(split_var[1:])




'''Q5 · Extract the city

Take address = "Madhapur, Hyderabad, Telangana". Extract and print only the city name — "Hyderabad" — which is between the first and second comma.

SAMPLE

Input:  address = "Madhapur, Hyderabad, Telangana"
Output: Hyderabad

'''




# address = "Madhapur, Hyderabad, Telangana"


# pos1 = address.find(",")

# pos2 = address.find(",",pos1 + 1)

# print(address[pos1+2:pos2])










'''Q6 · Extract the file extension

Take filename = "report.pdf". Using find() and slicing, extract and print only the extension — "pdf".

'''


# filename = "report.pdf"

# pos1 = filename.find(".")

# print(filename[pos1+1:])


















'''Q1 · Extract middle name

Take name = "Rahul Kumar Singh". Extract and print only the middle name — "Kumar".

SAMPLE

Input:  name = "Rahul Kumar Singh"
Output: Kumar

'''




'''
name = "Rahul Kumar Singh"

pos1 = name.find(" ")

pos2 = name.find(" ",pos1 + 1)

print(name[pos1+1:pos2])
'''













'''Q2 · Extract the month

Take date = "12-08-2005". Extract and print only the month — "08" — which is between the two dashes.

SAMPLE

Input:  date = "12-08-2005"
Output: 08
Input:  date = "25-12-2001"
Output: 12

'''






'''
date = "12-08-2005"


pos1 = date.find("-")

pos2 = date.find("-",pos1+1)

print(date[pos1 + 1:pos2])
'''










'''Q3 · Extract middle word

Take s = "cat-dog-fish". Extract and print the middle word — "dog" — which is between the two dashes.

SAMPLE

Input:  s = "cat-dog-fish"
Output: dog
Input:  s = "red-blue-green"
Output: blue
'''


'''
s = "cat-dog-fish"


pos1 = s.find("-")

pos2 = s.find("-",pos1+1)

print(s[pos1 + 1:pos2])


'''










'''Q4 · Extract text in brackets

Take s = "Hello (World) Python". Extract and print only the text inside the brackets — "World".

SAMPLE

Input:  s = "Hello (World) Python"
Output: World
Input:  s = "My (name) is Rahul"
Output: name
'''










'''
s = "Hello (World) Python"

pos1 = s.find("(")

pos2 = s.find(")",pos1 + 1)

print(s[pos1+1:pos2])

'''



















'''Q5 · Extract the folder name

Take path = "home/projects/python/file.txt". Extract and print only the second folder — "python" — between the second and third slash.

SAMPLE

Input:  path = "home/projects/python/file.txt"
Output: python

'''





'''
#right find fuction
path = "home/projects/python/file.txt"

pos1 = path.rfind("/")


pos2 = path.rfind("/",0,pos1)

print(path[pos2+1:pos1])
'''

















'''Q6 · Extract the day

Take date = "12-08-2005". Extract and print only the day — "12" — which comes before the first dash. Also extract the year — "2005" — which comes after the last dash.

SAMPLE

Input:  date = "12-08-2005"
Output: Day: 12
Year: 2005

'''

# date = "12-08-2005"

# pos1 = date.find("-")

# print("day: ",date[0:pos1 ])

# pos3 = date.split("-")

# print("year: ",pos3[2])












# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************


# Q1
# Easy
# Given name = 'Hyderabad', print its length, first character, and last character.
# 💡 Show Hint
# ✅ Show Solution

# name = 'Hyderabad'

# print(len(name))

# print(name[0])

# print(name[-1])











# Q2
# Easy
# Check if 'hello world' ends with 'world'. Print the result.
# 💡 Show Hint
# ✅ Show Solution


# var1 = 'hello world'
# print(var1.endswith("world"))










# Q3
# Easy
# Capitalize the first letter of 'python is fun'.
# 💡 Show Hint
# ✅ Show Solution


# var1 = "python is fun"
# print(var1.capitalize())













# Q4
# Easy
# Replace all spaces in 'hello world' with underscores.
# 💡 Show Hint
# ✅ Show Solution


# var1 = "hello world"
# print(var1.replace(" ", "_"))















# Q5
# Easy
# Count how many times 'l' appears in 'hello world'.
# 💡 Show Hint
# ✅ Show Solution



# var1 = "hello world"
# print(var1.count("l"))











# Q6
# Medium
# Extract 'world' from 'hello world' using slicing.
# 💡 Show Hint
# ✅ Show Solution



# var1 = "hello world"
# print(var1[6:])












# Q7
# Medium
# Reverse the string 'Python' using slicing.
# 💡 Show Hint
# ✅ Show Solution



# var1 = "python"
# print(var1[::-1])









# Q8
# Medium
# Find the position of 'world' in 'hello world'. What does find() return if not found?
# 💡 Show Hint
# ✅ Show Solution

# s = "hello world"
# var_find = s.find("world")
# print(var_find)

# RETURNS -1 IF FAILS










# Q9
# Medium
# Count how many times 'ab' appears in 'ababab'.
# 💡 Show Hint
# ✅ Show Solution


# s = "ababab"
# count1 = s.count("ab")
# print(count1)


# Q10
# Medium
# Extract every other character from 'abcdefgh' using slicing.
# 💡 Show Hint
# ✅ Show Solution


# s = "abcdefgh"
# print(s[::2])
# print(s[1::2])



# Q11
# Hard
# Prove strings are immutable. Try s[0] = 'H' for s = 'hello'. Then fix it.
# 💡 Show Hint
# ✅ Show Solution


# s = "hello"
# try:
#     s[0] = "H"
# except Exception as e:
#     print(e)


# Q12
# Hard
# Replace only the FIRST 'l' with 'L' in 'hello world'.
# 💡 Show Hint
# ✅ Show Solution


# word = 'hello world'
# print(word.replace("l","L",1))







# Q13
# Hard
# What does 'hello'[10] give? What about 'hello'[1:100]?
# 💡 Show Hint
# ✅ Show Solution




# 'hello'[10]   → Traceback (most recent call last):
#   File "e:\PyhtonProjects\strings_and_its_fuctions.py", line 771, in <module>
#     'hello'[10]
# IndexError: string index out of range

# print('hello'[1:100])   
# ello








# Q14
# Hard
# Count occurrences of each character in 'banana'.
# 💡 Show Hint
# ✅ Show Solution


# word = "banana"
# for i in set(word):
#     print(i, ":", word.count(i))










# Q15
# Hard
# Extract every character at an even index from 'Hello World Python'.
# 💡 Show Hint
# ✅ Show Solution



# sentence = 'Hello World Python'
# print(sentence[::2])



