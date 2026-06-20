# student_1 = ["karan",  23, 67.9]

# student_1[0] = "arjun"



# print(student_1[0:len(student_1)])










#list= [2,5,1]


# list = ["apple", "litchi"]

# list.reverse()
# print(list)










# list = [1,2,4,1]

# list.pop(0)

# print(list)


















#******************************************************************************************************************************


'''
Q1 · Add to the list

Take fruits = ["apple", "banana", "mango"]. Add "orange" to the end and print the updated list.

SAMPLE

Input:  fruits = ["apple", "banana", "mango"]
Output: ['apple', 'banana', 'mango', 'orange']

'''


# fruits = ["apple", "banana", "mango"]

# fruits.append("orange")

# print(fruits)





'''
Q2 · Insert at position

Take nums = [10, 20, 40, 50]. Insert 30 at index 2 so the list becomes [10, 20, 30, 40, 50].

SAMPLE

Input:  nums = [10, 20, 40, 50]
Output: [10, 20, 30, 40, 50]

'''


# nums = [10, 20, 40, 50]

# nums.insert(2,30)

# print(nums)








''''
Q3 · Remove an item

Take colors = ["red", "blue", "green", "blue"]. Remove "blue" from the list and print the result.

SAMPLE

Input:  colors = ["red", "blue", "green", "blue"]
Output: ['red', 'green', 'blue']
'''


# colors = ["red", "blue", "green", "blue"]

# colors.pop()

# print(colors)













'''
Q4 · Pop the last item

Take items = ["pen", "book", "bag", "bottle"]. Remove and print the last item. Then print the updated list.

SAMPLE

Input:  items = ["pen", "book", "bag", "bottle"]
Output: Removed: bottle
['pen', 'book', 'bag']

'''

'''
items = ["pen", "book", "bag", "bottle"]

removed = items.pop()

print("Removed:", removed)
print(items)

'''









''''
Q5 · Sort the list

Take nums = [5, 2, 8, 1, 9, 3]. Print the list sorted in ascending order, then in descending order.

SAMPLE

Input:  nums = [5, 2, 8, 1, 9, 3]
Output: [1, 2, 3, 5, 8, 9]
[9, 8, 5, 3, 2, 1]

'''


# nums = [5, 2, 8, 1, 9, 3]

# nums.sort()

# print(nums)

# nums.sort(reverse=True)
# print(nums)








# '''
# Q6 · Reverse the list

# Take letters = ["a", "b", "c", "d", "e"]. Reverse the list and print it.

# SAMPLE

# Input:  letters = ["a", "b", "c", "d", "e"]
# Output: ['e', 'd', 'c', 'b', 'a']
# '''



# letters = ["a", "b", "c", "d", "e"]


# letters.reverse()
# print(letters)









'''
Q7 · First and last item

Take nums = [10, 20, 30, 40, 50]. Print the first item and the last item using indexing. Then remove the last item using pop() and print the updated list.

SAMPLE

Input:  nums = [10, 20, 30, 40, 50]
Output: First: 10
Last: 50
[10, 20, 30, 40]


'''


# nums = [10, 20, 30, 40, 50]

# remove_second = nums.pop()

# print(f"first: {nums [0]}")

# print(f"second: {remove_second}")

# print(nums)











'''
Q8 · Build a list

Start with an empty list squares = []. Append the squares of numbers 1 to 5 one by one. Print the final list and its length.

SAMPLE

Input:  squares = []
Output: [1, 4, 9, 16, 25]
Length: 5
'''

# squares = []



# power1 = squares.append(1**2)

# power2 = squares.append(2**2)

# power3 = squares.append(3**2)

# power4 = squares.append(4**2)

# power5 = squares.append(5**2)

# print(squares)
# print(f"length:  {len(squares)}")














'''
Q9 · Remove and insert

Take nums = [3, 1, 4, 1, 5, 9]. Remove the first occurrence of 1, then insert 7 at index 0, then sort the list. Print after each step.

SAMPLE

Input:  nums = [3, 1, 4, 1, 5, 9]
Output: After remove: [3, 4, 1, 5, 9]
After insert: [7, 3, 4, 1, 5, 9]
After sort:   [1, 3, 4, 5, 7, 9]

'''



# nums = [3, 1, 4, 1, 5, 9]


# first_occurance = nums.remove(1)

# print(f"After remove: {nums}")

# insert = nums.insert(0,7)

# print(f"After insert: {nums}")

# sort = nums.sort()

# print(f"After sort: {nums}")







'''

Q10 · Student marks manager

Take marks = [85, 92, 78, 65, 90]. Do all of the following in order and print after each step: add 88 to the end, remove 65, insert 70 at index 1, pop the last item, sort in descending order.

SAMPLE

Input:  marks = [85, 92, 78, 65, 90]
Output: After append:  [85, 92, 78, 65, 90, 88]
After remove:  [85, 92, 78, 90, 88]
After insert:  [85, 70, 92, 78, 90, 88]
After pop:     [85, 70, 92, 78, 90]
After sort:    [92, 90, 85, 78, 70]
'''



# marks = [85, 92, 78, 65, 90]

# marks.append(88)

# print(f"After append:  {marks}")

# marks.remove(65)

# print(f"After remove:  {marks}")

# marks.insert(1,70)

# print(f"After insert:  {marks}")

# marks.pop()

# print(f"After pop:  {marks}")

# marks.sort(reverse=True)

# print(f"After sort:  {marks}")


















# # write a program ton ask users to enter names of their 3 favorite movies and store them in a list





# movies = []


# movies.append(input("enter frist movie: "))


# movies.append(input("enter second movie: "))


# movies.append(input("enter third movie: "))

# print(movies)









# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************




# Q1
# Easy
# Create a list of 5 fruits. Append 'mango'. Print the final list.
# 💡 Show Hint
# ✅ Show Solution



# fruits = ['apple','banana','grapes','dates','licthi']
# fruits.append('mango')
# print(fruits)




# Q2
# Easy
# Create [5,3,8,1,9,2]. Sort ascending. Print.
# 💡 Show Hint
# ✅ Show Solution


# nums = [5,3,8,1,9,2]
# nums.sort()
# print(nums)




# Q3
# Easy
# Create [1,2,3,4,5]. Reverse and print.
# 💡 Show Hint
# ✅ Show Solution


# nums = [1,2,3,4,5]
# nums.reverse()
# print(nums)  # [5,4,3,2,1]






# Q4
# Easy
# Remove and print the last element from [10,20,30,40].
# 💡 Show Hint
# ✅ Show Solution


# nums = [10,20,30,40]
# print(nums.pop(3))




# Q5
# Easy
# Insert 99 at index 2 in [1,2,3,4].
# 💡 Show Hint
# ✅ Show Solution



# nums = [1,2,3,4]
# nums.insert(2,99)
# print(nums)






# Q6
# Medium
# Remove first 3 from [1,3,5,3,7]. What if you call remove(99)?
# 💡 Show Hint
# ✅ Show Solution


# nums = [1,3,5,3,7]
# nums.remove(3)
# print(nums)  # [1,5,3,7]




# Q7
# Medium
# Predict:

# lst = [3,1,2]
# print(sorted(lst))
# print(lst)
# 💡 Show Hint
# ✅ Show Solution


# output: [1,2,3]
# output: [3,1,2]







# Q8
# Medium
# Pop element at index 1 from [10,20,30,40].
# 💡 Show Hint
# ✅ Show Solution



# num_list = [10,20,30,40]
# num_list.pop(1)
# print(num_list)





# Q9
# Medium
# Sort [5,3,8,1] in descending order.
# 💡 Show Hint
# ✅ Show Solution

# num_list = [5,3,8,1]
# num_list.sort(reverse=True)
# print(num_list)




# Q10
# Medium
# Predict:

# lst = [1,2,3]
# x = lst.pop()
# print(x)
# print(lst)
# 💡 Show Hint
# ✅ Show Solution

# 3
# [1,2]







# Q11
# Hard
# Predict:

# x = y = [1,2,3]
# x.append(4)
# print(y)
# 💡 Show Hint
# ✅ Show Solution

# [1, 2, 3, 4]





# Q12
# Hard
# What happens when pop() is called on an empty list?
# 💡 Show Hint
# ✅ Show Solution


# lst = []
# lst.pop()
# print(lst)

# IndexError: pop from empty list




# Q13
# Hard
# Sort a list of strings by length.
# 💡 Show Hint
# ✅ Show Solution


# list_str = ["hello", "me", "python"]
# list_str.sort(key=len)
# print(list_str)



# Q14
# Hard
# Append 99 to the second inner list in [[1,2],[3,4],[5,6]].
# 💡 Show Hint
# ✅ Show Solution

# nested_list = [[1,2],[3,4],[5,6]]
# nested_list[1].append(99)       # index 1 = second inner list
# print(nested_list)              # [[1,2],[3,4,99],[5,6]]



# Q15
# Hard
# Predict:

# lst = [1,2,3,2,1]
# lst.remove(2)
# lst.remove(1)
# print(lst)
# 💡 Show Hint
# ✅ Show Solution

# [3,2,1]


# Q15
# Hard
# Predict:

# lst = [1,2,3,2,1]
# lst.remove(2)
# lst.remove(1)
# print(lst)
# 💡 Show Hint
# ✅ Show Solution

# [3,2,1]