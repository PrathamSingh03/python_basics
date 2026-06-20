

# Grouping Practice Questions



# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************

# Q1 — Easy
# python# Loop through [10, 20, 30, 40, 50].
# # Print each number and its double.
# # Expected:
# # 10 doubled is 20
# # 20 doubled is 40 ...

# list_1 = [10,20,30,40,50]

# for num in list_1:
#     print(f"{num} doubled is {num*2}")





# Q2 — Easy
# python# Write a function count_above_ten(lst) that counts
# # how many numbers in the list are greater than 10.
# # Test with [5, 15, 3, 22, 8, 11]
# # Expected: 3



# def count_above_ten(lst):
#     count = 0
#     for num in lst:
#         if num > 10:    
#             count += 1
#     return count        

# print(count_above_ten([5, 15, 3, 22, 8, 11]))




# Q3 — Easy
# python# Count the frequency of each character in "hello"
# # using a dictionary. Print the result.
# # Expected: {'h':1, 'e':1, 'l':2, 'o':1}




# word = "hello"

# count = {}

# for i in word:
#     count[i] = count.get(i,0)+1
# print(count) 





# Q4 — Easy
# python# Write a function sum_odds(lst) that returns
# # the sum of all ODD numbers in the list.
# # Test with [1, 2, 3, 4, 5, 6, 7]
# # Expected: 16


# def sum_odds(lst):
#     total = 0           # start a running total
#     for i in lst:
#         if i % 2 != 0:
#             total += i  # ADD each odd number to total
#     return total        # return the accumulated sum

# print(sum_odds([1, 2, 3, 4, 5, 6, 7]))  # 16



# Q5 — Easy
# python# Loop through ["apple", "hi", "banana", "kiwi", "cherry"].
# # Print only words that have more than 5 characters.
# # Expected:
# # banana
# # cherry


# def five_characters (word_list):
#     for i in word_list:
#         if len(i)<=5:
#             pass
#         else:
#             print(i)

# five_characters(["apple", "hi", "banana", "kiwi", "cherry"])








# Q6 — Medium
# python# Write a function word_lengths(sentence) that takes a sentence
# # and returns a dictionary where key=word, value=length of word.
# # Test with "hello world python"
# # Expected: {'hello':5, 'world':5, 'python':6}

        
# def word_lengths(sentence):
#     count = {}

#     for word in sentence.split():
#         count[word] = len(word)

#     return count

# print(word_lengths("hello world python"))








# Q7 — Medium
# python# Count how many times each number appears in:
# # [1, 2, 3, 2, 1, 3, 3, 4, 1]
# # Store in a dictionary and print it.
# # Expected: {1:3, 2:2, 3:3, 4:1}

# def count_num (numbers):
#     count = {}

#     for i in numbers:
#         count[i] = count.get(i,0)+1
    
#     return count


# print(count_num([1, 2, 3, 2, 1, 3, 3, 4, 1]))








# Q8 — Medium
# python# Write a function squares_dict(lst) that takes a list of numbers
# # and returns a dictionary where key=number, value=its square.
# # Test with [2, 3, 4, 5]
# # Expected: {2:4, 3:9, 4:16, 5:25}


# def squares_dict(lst):
#     count = {}
#     for i in lst:
#         count.update({i:i **2})
#     return count
# print(squares_dict([2, 3, 4, 5]))






# Q9 — Medium
# python# Write a function starts_with_vowel(lst) that takes a list
# # of strings and returns a NEW list with only words
# # that start with a vowel (a, e, i, o, u).
# # Test with ["apple", "banana", "egg", "cherry", "orange", "grape"]
# # Expected: ['apple', 'egg', 'orange']

# def starts_with_vowel(lst):
#     starting = []
#     for word in lst:
#         if word[0] in 'aeiou':
#             starting.append(word)       

#     return starting

# print(starts_with_vowel(["apple", "banana", "egg", "cherry", "orange", "grape"]))




# Q10 — Medium
# python# Write a function group_by_length(words) that groups words
# # by their length into a dictionary.
# # key = length, value = list of words with that length
# # Test with ["hi", "cat", "dog", "elephant", "bee", "ok"]
# # Expected: {2:['hi','ok'], 3:['cat','dog','bee'], 8:['elephant']}


# def group_by_length(words):
#     result = {}
#     for word in words:
#         length = len(word)          # get length of current word

#         if length in result:
#             result[length].append(word)   # key exists → add to list
#         else:
#             result[length] = [word]       # key new → create new list

#     return result

# words = ["hi", "cat", "dog", "elephant", "bee", "ok"]
# print(group_by_length(words))









# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************

# 🟢 Filtering Questions (like Q9)
# Q1 — Very Easy
# python# Loop through [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Print only numbers greater than 5
# # Expected: 6 7 8 9 10

# lst = [1,2,3,4,5,6,7,8,9,10]

# for i in lst:
#     if i > 5:
#         print(i)



# Q2 — Easy
# python# Loop through ["cat", "elephant", "dog", "butterfly", "ant"]
# # Print only words that have exactly 3 letters
# # Expected:
# # cat
# # dog
# # ant

# def three_letters (lst):
#     for word in lst:
#         lenght = len(word)
#         if lenght == 3:
#             print(word)
#     return


# three_letters(["cat", "elephant", "dog", "butterfly", "ant"])







# Q3 — Easy
# python# Write a function keep_long(lst) that returns a NEW list
# # with only words that have 4 or more characters.
# # Test with ["hi", "hello", "ok", "world", "bye", "python"]
# # Expected: ['hello', 'world', 'python']

# def keep_long(lst):
#     nes_list = []         

#     for word in lst:
#         if len(word) >= 4:
#             nes_list.append(word)  

#     return nes_list       

# print(keep_long(["hi", "hello", "ok", "world", "bye", "python"]))









# Q4 — Easy
# python# Write a function ends_with_e(lst) that returns a NEW list
# # with only words that END with the letter 'e'.
# # Test with ["apple", "banana", "orange", "grape", "kiwi"]
# # Expected: ['apple', 'orange', 'grape']
# # Hint: word[-1] gives the last character


# def ends_with_e(lst):
#     new_lst = []

#     for word in lst:
#         if word[-1] == "e":
#             new_lst.append(word)

#     return new_lst

# print(ends_with_e(["apple", "banana", "orange", "grape", "kiwi"]))







# Q5 — Medium
# python# Write a function only_positive(lst) that returns a NEW list
# # with only positive numbers (greater than 0).
# # Then also return the COUNT of positive numbers.
# # Return both as a tuple: (list, count)
# # Test with [-3, 5, -1, 8, 0, 2, -4, 6]
# # Expected: ([5, 8, 2, 6], 4)

# def only_positive(lst):
    
#     new_lst = []
#     count = 0

#     for num in lst:
  
#         if num > 0:
#             new_lst.append(num)
#             count += 1
#             new_tup = (new_lst,count)
  
#     return new_tup

# print(only_positive([-3, 5, -1, 8, 0, 2, -4, 6]))




# 🔵 Grouping Questions (like Q10)
# Q6 — Very Easy — understand the pattern first
# python# You are given this empty dictionary:
# # result = {}
# # 
# # Add these words to it manually (no loop needed):
# # "cat"  → goes in key 3
# # "dog"  → goes in key 3
# # "hi"   → goes in key 2
# #
# # Expected result: {3: ['cat', 'dog'], 2: ['hi']}
# #
# # Hint: result[3] = ['cat']
# #       result[3].append('dog')
# #       result[2] = ['hi']



# result = {}            # start with empty dict

# result[3] = ['cat']    # key 3 → new list with 'cat'
# result[3].append('dog')# key 3 already exists → add 'dog'
# result[2] = ['hi']     # key 2 → new list with 'hi'

# print(result)
# # {3: ['cat', 'dog'], 2: ['hi']}



# Q7 — Easy
# python# Write a function group_evens_odds(lst) that groups numbers
# # into a dictionary with two keys: 'even' and 'odd'.
# # Test with [1, 2, 3, 4, 5, 6]
# # Expected: {'odd': [1, 3, 5], 'even': [2, 4, 6]}
# #
# # Hint: Start with result = {'even': [], 'odd': []}
# #       Then append to the right list

# def group_evens_odds(lst):

#     result = {'even': [], 'odd': []}

#     for num in lst:
#         if num % 2 == 0:
#             result.get('even',0).append(num)
#         else:
#             result.get('odd',0).append(num)
        
#     return result


# print(group_evens_odds([1, 2, 3, 4, 5, 6]))


# result['even'].append(num)          # ✅ simpler — you KNOW key exists

# Q8 — Medium
# python# Write a function group_by_first_letter(words) that groups
# # words by their first letter.
# # Test with ["apple", "ant", "banana", "cat", "cherry", "avocado"]
# # Expected: {'a':['apple','ant','avocado'], 'b':['banana'], 'c':['cat','cherry']}
# #
# # Hint: key = word[0]  ← first letter
# #       if key in result: append
# #       else: create new list

# def group_by_first_letter(words):

#     result = { 'a': [], 'b': [], 'c': [] }

#     for word in words:
#         if word[0] == "a":
#             result.get('a',0).append(word)
#         elif word[0] == "b":
#             result.get('b',0).append(word)
#         elif word[0] == "c":
#             result.get('c',0).append(word)
            
#     return result

# print(group_by_first_letter(["apple", "ant", "banana", "cat", "cherry", "avocado"]))





# def group_by_first_letter(words):
#     result = {}                      # start EMPTY — add keys dynamically

#     for word in words:
#         key = word[0]                # ✅ first letter

#         if key in result:
#             result[key].append(word) # key exists → add to list
#         else:
#             result[key] = [word]     # key new → create fresh list

#     return result

# print(group_by_first_letter(["apple","ant","banana","cat","cherry","avocado"]))
# # {'a':['apple','ant','avocado'], 'b':['banana'], 'c':['cat','cherry']}




# Q9 — Medium
# python# Write a function group_by_length(numbers) that groups numbers
# # by the number of digits they have.
# # Test with [1, 22, 333, 4, 55, 6666, 77]
# # Expected: {1:[1,4], 2:[22,55,77], 3:[333], 4:[6666]}
# #
# # Hint: len(str(number)) gives the number of digits

# def group_by_length(numbers):
#     result = {}

#     for number in numbers:
#         key = len(str(number))   # ✅ separate variable for digit count

#         if key in result:
#             result[key].append(number)   # ✅ append() with ()
#         else:
#             result[key] = [number]       # ✅ list with []

#     return result

# print(group_by_length([1, 22, 333, 4, 55, 6666, 77]))


# Q10 — Medium
# python# Write a function categorize_scores(scores) that groups scores
# # into grade categories using a dictionary.
# # A = 90 and above, B = 80-89, C = 70-79, F = below 70
# # Test with [95, 82, 67, 91, 75, 88, 55]
# # Expected: {'A':[95,91], 'B':[82,88], 'C':[75], 'F':[67,55]}
# #
# # Hint: Use if/elif/else to find grade.
# #       Then use the grouping pattern:
# #       if grade in result: append
# #       else: create new list


# def categorize_scores(scores):
#     grade_result = {}


#     for mark in scores:
            
#             if mark >= 90:
#                 grade_result.get('A',0).append(mark)
            
#             elif mark >= 80:
#                 grade_result.get('B',0).append(mark)
            
#             elif mark >= 70:
#                 grade_result.get('C',0).append(mark)
            
#             else:
#                 grade_result.get('F',0).append(mark)
            
#     return grade_result


# print(categorize_scores([95, 82, 67, 91, 75, 88, 55]))







