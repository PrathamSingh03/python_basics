

# t = ("Rahul", "Hyderabad", 21)

# name, age, city = t        # unpack into variables

# print(name)    # Rahul
# print(age)     # 21
# print(city)    # Hyderabad












# count how many A grades in the tupple and print the count. after that do sort them ascending order and store them in a new list


# grade = ("C", "D", "A", "A", "B", "B", "A")


# print(grade.count("A"))



# convert_list = list(grade)

# convert_list.sort()

# print(convert_list)












# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************



# Q1
# Easy
# Tuple of 3 colors. Print and length.
# 💡 Show Hint
# ✅ Show Solution

# tupple_color = ("red", "blue", "green")
# print(tupple_color)
# print(len(tupple_color))




# Q2
# Easy
# First and last of t=(10,20,30,40).
# 💡 Show Hint
# ✅ Show Solution

# t=(10,20,30,40)
# print(t[0],t[-1])


# Q3
# Easy
# Unpack (1,2,3) into x,y,z.
# 💡 Show Hint
# ✅ Show Solution

# var1 = (1,2,3)
# x,y,z = var1
# print(x)
# print(y)
# print(z)

# Q4
# Easy
# t=(1,3,5,3,3,7): count 3s and index of 5.
# 💡 Show Hint
# ✅ Show Solution

# t=(1,3,5,3,3,7)
# print(t.count(3))
# print(t.index(5))


# Q5
# Easy
# Predict:

# t1=(5,)
# t2=(5)
# print(type(t1))
# print(type(t2))
# 💡 Show Hint
# ✅ Show Solution

# <class 'tuple'>
# <class 'int'>


# Q6
# Medium
# Prove tuples are immutable.
# 💡 Show Hint
# ✅ Show Solution

# t=(1,3,5,3,3,7)
# t[1] = "2"
# TypeError: 'tuple' object does not support item assignment


# t=(1,2,3)
# try:
#     t[0]=99
# except TypeError as e:
#     print(e)





# Q7
# Medium
# Last 3 elements of (1,2,3,4,5).
# 💡 Show Hint
# ✅ Show Solution

# t = (1,2,3,4,5,6)
# print(t[-3:])





# Q8
# Medium
# Concatenate (1,2,3) and (4,5,6).
# 💡 Show Hint
# ✅ Show Solution

# print((1,2,3)+(4,5,6))







# Q9
# Medium
# Predict:

# t=(1,2,3)*3
# print(t.count(2))
# 💡 Show Hint
# ✅ Show Solution


# (1,2,3,1,2,3,1,2,3)
# output: 3






# Q10
# Medium
# sorted() on tuple — what type returns?
# 💡 Show Hint
# ✅ Show Solution

# print(type(sorted((3,1,2))))  
# list



# Q11
# Hard
# Predict:

# t=([1,2],3)
# t[0].append(4)
# print(t)
# 💡 Show Hint
# ✅ Show Solution

# ([1,2,4],3)


# Q12
# Hard
# Safe code when index() element not found.
# 💡 Show Hint
# ✅ Show Solution


# t = (1, 2, 3)
# try:
#     t.index(99)         
# except ValueError:
#     print('Not found')



# Q13
# Hard
# Unpack only first and last from 5-element tuple.
# 💡 Show Hint
# ✅ Show Solution



# # Intended way ✅ — unpacking in one line
# t = (1, 2, 3, 4, 5)
# first, *_, last = t
# print(first, last)   # 1 5




# Q14
# Hard
# Predict:

# t=(1,2,3,2,1)
# print(t.count(1)+t.index(2))
# 💡 Show Hint
# ✅ Show Solution


# t.count(1) = 2 (1 appears at index 0 and 4)
# t.index(2) = 1 (first 2 is at index 1)
# output: 3



# Q15
# Hard
# Convert tuple→list, modify, convert back.
# 💡 Show Hint
# ✅ Show Solution

# t=(1,2,3,2,1)
# list_con = list(t)

# list_con[-1] = 5
# print(list_con)

# tup_cov = tuple(list_con)
# print(type(tup_cov))

