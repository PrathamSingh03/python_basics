
'''
Q1 of 20
Strings Easy
Write a program that takes a string and prints it in reverse. Example: "hello" → "olleh"

'''









# name = "Hello"

# print(name[::-1])


'''
Q2 of 20
Strings Easy
Count the number of vowels (a, e, i, o, u) in a given string. Example: "python" → 2

'''


# name = "hello hi adam leon"

# print(name)


# print("a count:", name.count("a"))

# print("e count:", name.count("e"))

# print("i count:", name.count("i"))

# print("o count:", name.count("o"))

# print("u count:", name.count("u"))




'''
Q3 of 20
Strings Medium
Write a program to check if a given string is a palindrome (reads the same forwards and backwards). Example: "racecar" → True

'''

# car = "racecar"

# copy_car = car[::-1]



# if(car==copy_car):
#     print("palindrome")


# else:
#     print("not palindrome")








'''
Q2 · Shopping cart

Start with cart = ["bread", "milk", "eggs"]. Add "butter", remove "milk", then print the cart and how many items are in it.

SAMPLE

Input:  cart = ["bread", "milk", "eggs"]
Output: ['bread', 'eggs', 'butter']
Items: 3


'''


'''
cart = ["bread", "milk", "eggs"]

cart.append("butter")

cart.remove("milk")

print(cart)

print(f"Items: {len(cart)}")
'''










'''
Q3 · Student info

Take student = ("Arjun", 19, "CSE", 88). Unpack into name, age, branch, marks. Print each with a label. Also print the position of 88 in the tuple.

SAMPLE

Input:  student = ("Arjun", 19, "CSE", 88)
Output: Name: Arjun
Age: 19
Branch: CSE
Marks: 88
Position of 88: 3

'''

# student = ("Arjun", 19, "CSE", 88)

#name, age, Branch, Marks = student
# name = student[0]
# age = student[1]
# branch = student[2]
# marks = student[3]
'''
name, age, branch, marks = student

print(name)
print(age)
print(branch)
print(marks)

print(f"{student.index(88)}")

print(type(name))
'''



'''
Q4 · Traffic light

Take light = "red". Print "Stop" for red, "Get Ready" for yellow, "Go" for green, and "Invalid" for anything else.

SAMPLE

Input:  light = "red"
Output: Stop
Input:  light = "green"
Output: Go

'''




# light = "Green"



# if(light == "red"):
#     print("stop")

# elif(light == "yellow"):
#     print("wait")

# elif(light == "Green"):
#     print("GO")

# else:
#     print("light broken")


'''
Q5 · Word counter

Take s = "python is great and python is easy". Print how many times 'python' appears, replace 'python' with 'Java' and print, then print the total length of the original string.

SAMPLE

Input:  s = "python is great and python is easy"
Output: Count: 2
Java is great and Java is easy
Length: 34

'''





'''
s = "python is great and python is easy"

print(f"Count: {s.count("python")}")

print(s.replace("python","java").capitalize())

print(len(s))
'''












#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************
#*******************************************************************************************************************************************


# Q1
# Easy
# Variables
# Strings
# Type Casting
# Given age = '25' (a string), convert it to an integer, add 5, then print:
# 'In 5 years you will be 30'
# 💡 Show Hint
# ✅ Show Solution


# age = "25"
# con_age = int(age)
# print(f"In 5 years you will be {con_age + 5}")





# Q2
# Easy
# Lists
# Loops
# Operators
# Create a list [1, 2, 3, 4, 5]. Use a for loop to print each number and its square.
# 💡 Show Hint
# ✅ Show Solution


# for i in [1,2,3,4,5]:
#     print(f" the square of {i} = {i*i}")





# Q3
# Easy
# Strings
# Conditionals
# Slicing
# Check if the string 'racecar' is a palindrome (reads the same forwards and backwards). Print True or False.
# 💡 Show Hint
# ✅ Show Solution



# word  = 'racecar'
# if word[::-1] == word:
#     print(True)
# else:
#     print(False)









# Q4
# Easy
# Dictionary
# Loops
# Create a dictionary: name='Alice', age=20, city='Hyderabad'. Loop through it and print each key and value on one line.
# 💡 Show Hint
# ✅ Show Solution


# dict = {"name": "alice", "age" : 20, "City" : "Hyderabad"}

# for key,values in dict.items():
#     print(key, ":", values)









# Q5
# Easy
# Sets
# Lists
# Type Casting
# Given the list [3, 1, 2, 2, 3, 4, 1], remove duplicates and print the result as a sorted list.
# 💡 Show Hint
# ✅ Show Solution


# nums = [3, 1, 2, 2, 3, 4, 1]
# convert = sorted(set(nums))
# print(convert)







# Q6
# Easy
# Tuples
# Conditionals
# Variables
# Unpack person = ('Alice', 16) into name and age. Print 'Alice is an adult' or 'Alice is a minor' based on age.
# 💡 Show Hint
# ✅ Show Solution

# person = ('Alice', 16)

# name,age = person

# if age < 18:
#     print(name," is a minor")
# else:
#     print(name," is an adult")








# Q7
# Easy
# Functions
# Operators
# Conditionals
# Write a function is_divisible(n, x) that returns True if n is divisible by x, else False. Test with (10, 2) and (10, 3).
# 💡 Show Hint
# ✅ Show Solution


# def is_divisible(n, x):
#     if n%x==0:
#         print(True)
#     else:
#         print(False)

# is_divisible(10,3)


# def is_divisible(n, x):
#     return n % x == 0  # ✅ return the value

# print(is_divisible(10, 2))  # True
# print(is_divisible(10, 3))  # False





# Q8
# Easy
# Strings
# Loops
# Variables
# Count how many vowels are in the sentence 'Hello World' using a for loop and a counter variable.
# 💡 Show Hint
# ✅ Show Solution

# word = "Hello World"

# count = 0

# for ch in word.lower():
#     if ch in 'aeiou':
#         count+=1
# print(count)








# Q9
# Easy
# Lists
# Conditionals
# Loops
# From the list [10, -3, 5, -8, 2, -1, 7], create a new list with only the positive numbers. Print it.
# 💡 Show Hint
# ✅ Show Solution



# list1 = [10, -3, 5, -8, 2, -1, 7]

# new_list1 = []

# for ch in list1:
#     if ch>0:
#         new_list1.append(ch)
# print(f"numbers added {new_list1}")







# Q10
# Easy
# Type Casting
# Strings
# Variables
# Convert pi = 3.14159 to a string. Print its length and extract and print just the first 4 characters.
# 💡 Show Hint
# ✅ Show Solution


# pi = 3.14159
# pi_str = str(pi)           
# print(len(pi_str))         
# print(pi_str[:4])   





# Q11
# Medium
# Functions
# Lists
# Conditionals
# Write a function get_evens(lst) that takes a list of numbers and returns a NEW list containing only the even numbers. Test with [1, 2, 3, 4, 5, 6, 7, 8].
# 💡 Show Hint
# ✅ Show Solution



# def get_evens (lst):
#     new_lst = []

#     for i in lst:
#         if lst%2==0:
#             new_lst.append(i)
#     return new_lst

# print(get_evens[(1,2,3,4)])



# Q12
# Medium
# Dictionary
# Loops
# Strings
# Count word frequency in 'the cat sat on the mat the cat'. Store counts in a dictionary and print it.
# 💡 Show Hint
# ✅ Show Solution

# word = 'the cat sat on the mat the cat'

# count = {}

# for i in word.split():
#     count[i] = count.get(i, 0) + 1 
# print(count)






# Q13
# Medium
# Functions
# Strings
# Conditionals
# Slicing
# Write a function is_palindrome(s) that ignores case and spaces, then returns True if the string is a palindrome.
# 💡 Show Hint
# ✅ Show Solution


# def is_palindrome(s):
#     clean_space = s.replace(" ", "").lower()
#     return clean_space == clean_space[::-1]  
                                             
# print(is_palindrome('racecar'))                       
# print(is_palindrome('A man a plan a canal Panama'))    
# print(is_palindrome('hello'))                         






# Q14
# Medium
# Functions
# Lists
# Sorting
# Write a function longest_first(words) that takes a list of words and returns them sorted by length, longest first.
# 💡 Show Hint
# ✅ Show Solution
# Q15
# Medium
# Tuples
# Dictionary
# Loops
# Conditionals
# Given scores = [('Alice',90), ('Bob',75), ('Carol',92), ('Dave',85)], convert to a dictionary and print the name of the highest scorer.
# 💡 Show Hint
# ✅ Show Solution
# Q16
# Medium
# Functions
# Type Casting
# Strings
# Loops
# Write a function str_to_sum(s) that takes a string of space-separated numbers like '1 2 3 4 5', converts them to integers, and returns their sum.
# 💡 Show Hint
# ✅ Show Solution
# Q17
# Medium
# Sets
# Functions
# Conditionals
# Write a function has_common(lst1, lst2) that returns True if the two lists share at least one common element, else False.
# 💡 Show Hint
# ✅ Show Solution
# Q18
# Medium
# Lists
# Loops
# Conditionals
# Variables
# Find the second largest number in [5, 1, 8, 3, 9, 2, 7] WITHOUT using sort(). Use a loop.
# 💡 Show Hint
# ✅ Show Solution
# Q19
# Medium
# Strings
# Dictionary
# Loops
# Count the frequency of each character in 'banana'. Store in a dictionary. Skip spaces if any. Print sorted by character.
# 💡 Show Hint
# ✅ Show Solution
# Q20
# Medium
# Functions
# *args
# Loops
# Conditionals
# Write a function filter_evens(*args) that takes any number of integers and returns a list of only the even ones.
# 💡 Show Hint
# ✅ Show Solution
# Q21
# Hard
# Functions
# Recursion
# Conditionals
# Write a recursive function fibonacci(n) that returns the nth Fibonacci number (0,1,1,2,3,5,8...). Then print the first 8 numbers.
# 💡 Show Hint
# ✅ Show Solution
# Q22
# Hard
# Lists
# Dictionary
# Loops
# Strings
# Group these words by their first letter into a dictionary:
# ['apple','banana','cherry','avocado','blueberry','carrot','apricot']
# 💡 Show Hint
# ✅ Show Solution
# Q23
# Hard
# Functions
# Lambda
# Lists
# Sorting
# Dictionary
# Given students = [{'name':'Alice','score':85},{'name':'Bob','score':92},{'name':'Carol','score':78}], sort them by score from highest to lowest using a lambda.
# 💡 Show Hint
# ✅ Show Solution
# Q24
# Hard
# Strings
# Functions
# Loops
# Dictionary
# Conditionals
# Write most_common_word(sentence) that returns the most frequently appearing word in a sentence. Ignore case.
# 💡 Show Hint
# ✅ Show Solution
# Q25
# Hard
# Lists
# Functions
# Loops
# Conditionals
# Type Casting
# Write flatten(lst) that converts a nested list [[1,2],[3,[4,5]],6] into a flat list [1,2,3,4,5,6]. Handle one level of nesting.
# 💡 Show Hint
# ✅ Show Solution
# Q26
# Hard
# Dictionary
# Functions
# Loops
# Conditionals
# Write invert_dict(d) that swaps keys and values. If two keys have the same value, keep both original keys in a list.

# Example: {'a':1,'b':2,'c':1} → {1:['a','c'], 2:['b']}
# 💡 Show Hint
# ✅ Show Solution
# Q27
# Hard
# Functions
# Loops
# Conditionals
# Sets
# Write primes_up_to(n) that returns a list of all prime numbers up to n. A prime is only divisible by 1 and itself.
# 💡 Show Hint
# ✅ Show Solution
# Q28
# Hard
# Strings
# Functions
# Loops
# Type Casting
# Conditionals
# Write caesar_cipher(text, shift) that shifts each letter forward by n positions. Keep non-letters unchanged.

# Example: caesar_cipher('hello', 3) → 'khoor'
# 💡 Show Hint
# ✅ Show Solution
# Q29
# Hard
# Functions
# Dictionary
# Lists
# Loops
# Conditionals
# Write grade_report(scores) that takes a list of scores and returns a dictionary with:
# - 'average' (rounded to 1 decimal)
# - 'grade' (A>=90, B>=80, C>=70, else F)
# - 'passed' (True if average >= 60)
# - 'highest' and 'lowest'
# 💡 Show Hint
# ✅ Show Solution
# Q30
# Hard
# Functions
# Dictionary
# Lists
# Sets
# Strings
# Loops
# Build a contact book using a dictionary. Write 3 functions:
# 1. add_contact(book, name, phone) — adds a contact
# 2. search_contact(book, name) — returns phone or 'Not found'
# 3. all_contacts(book) — prints all contacts sorted alphabetically





# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************

"""Here are 10 questions focused on string processing + functions — same skills as Q13:
"""


# Q1 — Easy
# python# Write a function reverse_word(word) that returns
# # the word reversed.
# # Test with "hello" → "olleh"
# # Test with "python" → "nohtyp"


# def reverse_word (word):
#     return word[::-1]
# print(reverse_word("hello"))




# Q2 — Easy
# python# Write a function is_same(s1, s2) that returns True
# # if both strings are equal IGNORING case.
# # Test:
# # is_same("Hello", "hello") → True
# # is_same("Python", "java") → False
# # Hint: use .lower() on both before comparing


# def is_same(s1, s2):
#     return s1.lower() == s2.lower()  

# print(is_same("Hello", "hello"))   
# print(is_same("Python", "java"))   


# Q3 — Easy
# python# Write a function count_spaces(s) that counts
# # how many spaces are in a string.
# # Test with "hello world python" → 2
# # Test with "no spaces" → 1
# # Hint: use .count(" ")

# def count_spaces(s):
#     count_spaces1 = s.count(" ")
    
#     return count_spaces1

# print(count_spaces("no spaces"))




# Q4 — Easy
# python# Write a function remove_vowels(word) that returns
# # the word with all vowels removed.
# # Test with "hello" → "hll"
# # Test with "python" → "pythn"
# # Hint: loop through each character,
# #       only keep it if NOT in 'aeiou'


# def remove_vowels(word):

#     result = ""
#     for vowel in word:
#         if vowel in "aeiou":
#             pass
#         else:
#             result+=vowel

#     return result

# print(remove_vowels("hello"))




# Q5 — Medium
# python# Write a function is_anagram(s1, s2) that returns True
# # if two strings are anagrams of each other.
# # (Anagram = same letters, different order)
# # Test:
# # is_anagram("listen", "silent") → True
# # is_anagram("hello", "world")  → False
# # Hint: sort both strings and compare
# #       sorted("listen") == sorted("silent")

# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# print(is_anagram("listen", "silent"))


# Q6 — Medium
# python# Write a function capitalize_words(sentence) that
# # capitalizes the FIRST letter of every word.
# # Test with "hello world python" → "Hello World Python"
# # Hint: use .split() to get words,
# #       use word[0].upper() + word[1:] for each word,
# #       use " ".join() to put back together

# def capitalize_words(sentence):
#     words = sentence.split()  
#     result = []

#     for word in words:
#         capitalized = word[0].upper() + word[1:]  
#         result.append(capitalized)

#     return " ".join(result)    

# print(capitalize_words("hello world python"))


# Q7 — Medium
# python# Write a function count_each_vowel(word) that returns
# # a dictionary with count of each vowel in the word.
# # Only include vowels that actually appear.
# # Test with "hello" → {'e':1, 'o':1}
# # Test with "banana" → {'a':3}
# # Hint: loop through word, check if ch in 'aeiou',
# #       use dict.get(ch, 0) + 1


# def count_each_vowel(word):
#     result = {}
#     for ch in word:
#         if ch in 'aeiou':
#             result[ch] = result.get(ch, 0) + 1   # ✅ count pattern
#     return result

# print(count_each_vowel('hello'))  # {'e':1, 'o':1}




# Q8 — Medium
# python# Write a function longest_word(sentence) that returns
# # the longest word in the sentence.
# # If two words are same length, return the first one.
# # Test with "I love python programming" → "programming"
# # Hint: split() to get words,
# #       loop and track the longest so far

# Q9 — Medium
# python# Write a function is_palindrome_number(n) that checks
# # if a NUMBER is a palindrome.
# # Test:
# # is_palindrome_number(121)  → True
# # is_palindrome_number(123)  → False
# # is_palindrome_number(1221) → True
# # Hint: convert to string first using str(),
# #       then check if s == s[::-1]

# Q10 — Hard
# python# Write a function most_frequent_char(s) that returns
# # the character that appears most often in a string.
# # Ignore spaces. Ignore case.
# # If two chars appear same times, return the first one found.
# # Test with "hello world" → 'l'
# # Test with "aabbcc" → 'a'
# # Hint:
# # 1. clean: s.replace(" ","").lower()
# # 2. count each char in a dict
# # 3. find the key with the highest value