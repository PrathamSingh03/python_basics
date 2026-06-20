
# set1 = {1,2,3,3,"world"}

# print(set1.add(4))

# print(set1.remove(3))


# set2 = set()

# set2.add(1)
# set2.add(2)
# set2.add(3)

# set2.remove(2)
# print(set2)



# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************
# *******************************************************************************************************************************************



# Q1
# Easy
# {1,2,2,3,3} — print and length.
# 💡 Show Hint
# ✅ Show Solution

# set1 = {1,2,2,3,3}

# print(set1)
# print(len(set1))




# Q2
# Easy
# Add 6 to {1,2,3,4,5}. Add 3 again.
# 💡 Show Hint
# ✅ Show Solution

# set_1 = {1,2,3,4,5}

# set_1.add(6)
# set_1.add(3)
# print(set_1)





# Q3
# Easy
# Common elements of {1,2,3,4} and {3,4,5,6}.
# 💡 Show Hint
# ✅ Show Solution


# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6}
# concat = set_1.intersection(set_2)
# print(concat)




# Q4
# Easy
# Combine {1,2,3} and {3,4,5}.
# 💡 Show Hint
# ✅ Show Solution


# set_1 = {1,2,3}
# set_2 = {3,4,5}
# combine = set_1.union(set_2)
# print(combine)







# Q5
# Easy
# Remove 3 from {1,2,3,4}. Then clear.
# 💡 Show Hint
# ✅ Show Solution

# set_1 = {1,2,3,4}
# set_1.remove(3)
# print(set_1)   

# set_1.clear()   
# print(set_1)   






# Q6
# Medium
# Elements in {1,2,3,4,5} NOT in {3,4,5,6,7}.
# 💡 Show Hint
# ✅ Show Solution



# set_1 = {1,2,3,4,5}
# set_2 = {3,4,5,6,7}

# diff = set_1.difference(set_2)
# print(diff)






# Q7
# Medium
# Predict:

# s={1,2,3}
# s.add(3)
# print(len(s))
# 💡 Show Hint
# ✅ Show Solution

# output: 3

# Q8
# Medium
# Add [1,2] to set. Then add (1,2).
# 💡 Show Hint
# ✅ Show Solution



# set_1 = {1, 2}

# # Try adding a LIST
# try:
#     set_1.add([1, 2])        
# except TypeError as e:
#     print(e)                 

# # Then add a TUPLE — this works
# set_1.add((1, 2))           
# print(set_1)               







# Q9
# Medium
# remove() vs discard() difference.
# 💡 Show Hint
# ✅ Show Solution



# s = {1, 2, 3}
# s.remove(9)    # ❌ KeyError — 9 not in set!
# s.discard(9)   # ✅ No error — silently ignored






# Q10
# Medium
# Remove duplicates from [1,3,2,3,1,4,2] preserving order.
# 💡 Show Hint
# ✅ Show Solution

# not understanding


# lst = [1, 3, 2, 3, 1, 4, 2]
# seen = set()
# result = []
# for x in lst:
#     if x not in seen:   # only add if not seen before
#         seen.add(x)
#         result.append(x)
# print(result)   # [1, 3, 2, 4] — order preserved!
# # Can't just do set(lst) because sets are unordered




# Q11
# Hard
# Elements in EITHER but NOT both: {1,2,3} ^ {2,3,4}
# Elements in EITHER but NOT both: {1,2,3} ^ {2,3,4}

# 💡 Show Hint
# ✅ Show Solution

# not undersanidng


# Elements in EITHER set but NOT in BOTH
# print({1,2,3} ^ {2,3,4})   # {1, 4}
# 1 is only in first set ✓
# 2 and 3 are in BOTH — excluded ✗
# 4 is only in second set ✓




# Q12
# Hard
# {1,2} subset of {1,2,3,4}?
# 💡 Show Hint
# ✅ Show Solution

# not undersanidng


# # Is every element of {1,2} inside {1,2,3,4}?
# print({1,2} <= {1,2,3,4})          # True
# print({1,2}.issubset({1,2,3,4}))   # True
# print({1,5} <= {1,2,3,4})          # False — 5 not in bigger set




# Q13
# Hard
# Predict:

# s1={1,2,3};s2={4,5,6}
# print(s1.intersection(s2))
# print(s1|s2)
# 💡 Show Hint
# ✅ Show Solution

# # not undersanidng


# s1={1,2,3}; s2={4,5,6}
# print(s1.intersection(s2))  # set() — no common elements!
# print(s1|s2)                 # {1,2,3,4,5,6} — all combined

# Q14
# Hard
# sorted() on set — what type?
# 💡 Show Hint
# ✅ Show Solution

# print(type(sorted({3,1,2})))
# class : list


# Q15
# Hard
# Why can't you predict which element pop() removes?
# 💡 Show Hint
# ✅ Show Solution

# Sets are unordered.



