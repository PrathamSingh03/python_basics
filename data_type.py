# 2. Data Types







# Easy

# Create variables of type int, float, string, bool and print their types.

# var1 = 1

# var2= 2.3

# var3 = "hi"

# var4 = True

# print(f"variable 1 is {type(var1)}, variable 2 is {type(var2)}, variable 3 is {type(var3)}, variable 4 is {type(var4)} ")





# Create a list of 5 favorite movies.


# fav_movies = ["avatar", "fast and furious", "rambo", "rocky", "a way out", ]


# print(fav_movies)








# Create a tuple of weekdays.


# weekday = ("mon","tue","wed","thur","fri")

# print(weekday)






# # Create a set of numbers.


# set_1 = {1,2,3,4,5,6}

# print(set_1)




# # Create a dictionary storing student details.

# student_details_dict = {"name" : "pratham singh",
                        
#                         "age" : 25,
                        
                        
                        
#                         "subjects and marks": {
#                             "maths" : 55,
#                             "english": 52,
#                             "hindi": 54
#                         },
                        
#                         "class": "X standerd"
#                         }

# print(student_details_dict)













# Medium


# Take input from user and print its data type.



# user_input = input("Enter here: ")

# if user_input.isdigit():
#     print("Your entered input is integer type")

# elif "." in user_input:
#     print("Your entered input is float type")

# elif user_input == "True" or user_input == "False":
#     print("Your entered input is boolean type")

# else:
#     print("Your entered input is string type")














# Create a mixed data type list.



# mix_list = [1,2.3,True,"str"]

# mix_list[3] = "hello"




# Create nested list and access inner elements.

# nest_list = [1, [11,22,33], 2,3,4,5]

# print(nest_list[1][1])



# Create dictionary with multiple students.

# student_dict = {

#     "name": ["pratham", "salman", "vijay"],

#     "age": [25, 23, 26]
# }

# print(student_dict["name"][1])




# Convert tuple into list and add values.


# tup1 = (1,2,3,4,5,6)

# convert_li = list(tup1)


# convert_li.insert(4,4.5)

# print(convert_li)









# Hard


# Create mini phonebook using dictionary.


# phonebook = {
#     "pratham": 9876543210,
#     "salman": 9123456780
# }

# print(phonebook["salman"])






# Create shopping cart using list.


# items = []

# end_shopping = "done"

# while True:
#     select_items = input("select items: ")

#     if select_items == end_shopping:
#         print("all shoping done")
#         break

#     else:
#         items.append(select_items)


# print(f"you have seleetd these {len(items)} items: {items} ")






# Store marks of students in dictionary and print highest marks.



# student_dict = {

#     "name": ["pratham", "salman", "vijay"],

#     "marks": [25, 23, 26]
# }


# print(max(student_dict["marks"]))














# Create set operations program.


# set1 = {1,2,3}

# set2 = {3,4,5}

# print(f"operation 1 {set1.intersection(set2)}")

# print(f"operation 2 {set1.union(set2)}")

# print(f"operation 3 {set1.difference(set2)}")














# Build small inventory system using dictionary.


# inventory = {

#     "products" : {
#         "apple" : 5,
#         "mango" : 4,
#         "grapes" : 9
#     }
# }

# while True:

#     enter_product = (input("enter product: "))

#     if enter_product in inventory['products'].keys():
#         new_stock = int(input("enter new quantity: "))
#         inventory["products"][enter_product]+=new_stock
#         print(f" current inventory:>    {inventory}")
#         break















