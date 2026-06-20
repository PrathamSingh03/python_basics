

# nested dictionnary
# student = {

#     "name" : "pratham singh",
#     "score" : {
#         "maths" : {
#             "1st semester" : 33,
#             "2nd semster" : 33,
#         },
#         "physics" : 90,
#         "chem": 85,
#     },
#     "age" : 55

# }


# print(dict["score"]["maths"])




# dictonary_names.keys() returns all keys specific dictinaary

# print(dict.keys())


# dict.values() returns the values in the dictanries

# print(dict.values())



# print(student.get("name"))



# student["city"] = "delhi"


# print(student.update({"state" : "HR"}))    























'''
Q1
Adding keys
easy
Build a student record
Create an empty dictionary called student. Add the following keys one by one: 'name' → 'Aarav', 'age' → 18, 'grade' → 'B+'. Then print the final dictionary.
student = {}
Expected output: {'name': 'Aarav', 'age': 18, 'grade': 'B+'}

'''
'''
student = {}


student["name"] = "Aarav"
student["age"] = "18"
student["grade"] = "B+"



print(student)
'''











'''
Q2
.keys() / .values()
easy
Count keys and sum values
Given the dictionary below, write code to: (1) print how many keys it has, (2) print the sum of all values.
marks = {"Math": 80, "Science": 90, "English": 70, "History": 85}
Expected output: 4 | 325

'''


# marks = {"Math": 80, "Science": 90, "English": 70, "History": 85}

# print(f"{len(marks.keys())} | {sum(marks.values())}")















'''
Q3
.get()
easy
Safe profile lookup
Write a program that asks for a key to look up in the dictionary. If the key exists, print its value. If not, print 'Key not found'. Use .get() — no if/else needed.
profile = {"name": "Diya", "city": "Chennai", "hobby": "painting"}
key = input("Enter key: ")
Expected output: # If user types 'city' → Chennai | # If user types 'age' → Key not found

'''

'''
profile = {"name": "Diya", "city": "Chennai", "hobby": "painting"}
key = input("Enter key: ")

print(profile.get(key, "Key not found"))
'''












'''

Q4
.items()
medium
Find the highest scorer
Loop through the dictionary using .items() and find the student with the highest marks. Print their name and score.
scores = {"Meera": 88, "Arjun": 95, "Sneha": 91, "Kiran": 78}
Expected output: Arjun: 95


'''




'''

Q5
.update()
medium
Merge and update cart
You have an existing cart and a new order. Use .update() to merge them. Items in new_order should overwrite existing ones if they already exist. Print the final cart.
cart = {"apple": 3, "banana": 2, "mango": 1}
new_order = {"banana": 5, "grapes": 4}
Expected output: {'apple': 3, 'banana': 5, 'mango': 1, 'grapes': 4}

'''

# cart = {"apple": 3, "banana": 2, "mango": 1}
# new_order = {"banana": 5, "grapes": 4}


# cart.update(new_order)

# print(cart)







'''
Q6
.items() + logic
medium
Filter passing students
Create a new dictionary called passed that contains only students who scored 50 or above. Print the new dictionary.
results = {"Ali": 45, "Priya": 78, "Sam": 50, "Tara": 30, "Rohan": 65}
Expected output: {'Priya': 78, 'Sam': 50, 'Rohan': 65}

'''
















'''
WAP to enter marks of 3 subjets form the user and store them in a dictionary. start with and empty dictnary and add one by one .
use subjects name as key and marks as values. 

'''


# class1 = {}

# sub1 = int(input("english marks: "))
# class1.update({"english" : sub1})

# sub2 = int(input("maths marks: "))
# class1.update({"maths" : sub2})
              
# sub3 = int(input("hindi marks: "))
# class1.update({"hindi : " : sub3})


# print(class1)









# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************



# Q1
# Easy
# Student dict: name='Alice',age=20,grade='A'. Print name.
# 💡 Show Hint
# ✅ Show Solution


# student = {"name" : 'Alice', "age" : 20, "grade" : 'A'}
# print(student.get("name"))




# Q2
# Easy
# Keys and values of {'a':1,'b':2,'c':3}.
# 💡 Show Hint
# ✅ Show Solution


# d={'a':1,'b':2,'c':3}
# print(d.keys())
# print(d.values())



# Q3
# Easy
# get() missing key 'email'. Return 'Not provided'.
# 💡 Show Hint
# ✅ Show Solution

# student = {"name" : 'Alice', "age" : 20, "grade" : 'A'}
# print(student.get("email","not provided"))






# Q4
# Easy
# Add two pairs using update().
# 💡 Show Hint
# ✅ Show Solution

# student = {"name" : 'Alice', "age" : 20, "grade" : 'A'}
# student.update({"email" : "alice@gmail.com"})
# student.update({"roll no." : "22"})
# print(student)





# Q5
# Easy
# Iterate dict and print each key-value.
# 💡 Show Hint
# ✅ Show Solution


# student = {"name" : 'Alice', "age" : 20, "grade" : 'A'}
# for k, v in student.items():
#     print(k, ':', v)








# Q6
# Medium
# Access city in nested dict:
# d={'user':{'address':{'city':'Hyderabad'}}}
# 💡 Show Hint
# ✅ Show Solution



# d={'user':{'address':{'city':'Hyderabad'}}}
# print(d['user']['address']['city'])


# Q7
# Medium
# Safely delete 'age'. Handle if missing.
# 💡 Show Hint
# ✅ Show Solution

# student = {"name" : 'Alice', "age" : 20, "grade" : 'A'}
# remove = student.pop("age",0)
# print(student)






# Q8
# Medium
# Predict:

# d={'a':1,'b':2}
# d.update({'b':99,'c':3})
# print(d)
# 💡 Show Hint
# ✅ Show Solution

# {'a':1,'b':99,'c':3}


# Q9
# Medium
# Word frequency in 'the cat sat on the mat the cat'.
# 💡 Show Hint
# ✅ Show Solution


# not able to solve







# Q10
# Medium
# Predict:

# d={'a':1}
# print(d['b'] if 'b' in d else -1)
# print(d.get('b'))
# print(d.get('b',0))
# 💡 Show Hint
# ✅ Show Solution

# output: -1
# None
# 0




# Q11
# Hard
# Change city 'Mumbai'→'Delhi'.
# 💡 Show Hint
# ✅ Show Solution

# d={'user':{'city':'Mumbai'}}

# d['user']['city'] = "delhi"
# print(d)



# Q12
# Hard
# Merge {'a':1,'b':2} and {'b':3,'c':4}. Second overrides.
# 💡 Show Hint
# ✅ Show Solution

# d1={'a':1,'b':2}
# d1.update({'b':3,'c':4})
# print(d1)



# Q13
# Hard
# Keys where value>2 from {'a':1,'b':3,'c':2,'d':5}.
# 💡 Show Hint
# ✅ Show Solution

# d={'a':1,'b':3,'c':2,'d':5}

# result = []

# for k, v in d.items():
#     if v > 2:
#         result.append(k)

# print(result)


# Q14
# Hard
# d['b'] on d={'a':1} — what happens?
# 💡 Show Hint
# ✅ Show Solution


# d={'a':1}
# try:
#     print(d['b'])
# except KeyError:
#     print('KeyError')



# Q15
# Hard
# Nested dict for 2 students. Access Bob's first score.
# 💡 Show Hint
# ✅ Show Solution


# stu = {"adam": {"scores": [34,78],},"bob": {"scores": [55,48]} }
# print(stu["bob"]["scores"][0])                                
                            





