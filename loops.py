#while loop

#for increment

'''
i = 1

while i<=5:
    print(i)
    i+=1
'''


# for decrement
'''
i = 5

while i>=1:
    print(i)
    i-=1
'''


'''
table of 2 below
'''

'''
number = int(input("enter number: "))
num_1 = 1

while num_1<=10:
    print(num_1*number)
    num_1+=1
'''














'''
print these list numbers from starting to end using while loop

'''

'''

a = [1,4,9,16,25,36,49,64,81,100]

index = 0
while index < len(a):
    print(a[index])
    index+=1
'''




'''
search for a number X in this tupple using loop
'''


'''
a = (1,4,9,16,25,36,49,64,81,100)

x = 25

i= 0

while i < len(a):
    if(a[i]==x):
        print("found at index: ", i)
    i+=1
'''




'''
while basics
Q1. Count down from 10

Write a while loop that prints numbers from 10 down to 1 (inclusive), each on a new line.

'''


# i = 10

# while i>= 1:
#     print("number: ", i)
#     i-=1






'''
while basics
Q2. Sum of digits

Take a positive integer n. Use a while loop to find the sum of all integers from 1 to n.
'''
'''
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)
'''


# n = 12

# total = 0    # stores the running sum
# index = 1    # start from 1 (not 0, since sum is 1 to n)

# while index <= n:
#     total += index   # add current number to total
#     index += 1       # move to next number

# print(f"Sum from 1 to {n} is: {total}")









'''

i = 2

while i <=10:
    print(i)
    i+=2
'''


'''
Q3. Count how many times you can halve 64

Start with n = 64. Keep dividing it by 2 until it reaches 1. Count how many divisions you did.

Think before coding:
Start → n = 64, count = 0
Stop when → n equals 1
Each step → divide n by 2, add 1 to count
'''




'''
n = 64
count = 0
while n > 1:
    n = n // 2
    count += 1
print(count)
'''






# n = 1

# count = 0

# while n != 32:
#     n=n*2
#     count+=1

# print(count)





# n = 64

# total = 0

# while n>1:
#     n = n//2
#     total = n+total
    

# print(total)








'''
Q4. Multiply until over 100

Start with n = 1. Keep multiplying by 3 each step. Count how many multiplications it takes for n to exceed 100.

Think before coding:
Start → n = 1, count = 0
Stop when → n exceeds 100
Each step → multiply n by 3, add 1 to count

'''

'''
n = 1

count = 0

while n < 100:
    n=n*3
    count+=1

print(count)
'''
















'''
Q5. Stop at the first number divisible by 7

Go through numbers 1 to 50. As soon as you find a number divisible by 7, print it and stop.

Think before coding:
Check each number → is i % 7 == 0?
If yes → print it and break
If no → keep going

'''


'''

n = 1

count = 0

while n <= 50:
    if(n%7==0):
        print(f"divisible by 7,{n}")
        break

    else:
        print("finding")  

count+=1


'''


'''
count = 1
while count <= 50:
    print(f"value of count is {count}")
    if(count%7==0):
        print(f"divisible by 7 is this number-> {count}")
        break
    else:
        print("finding")
        count = count+1
'''


















'''
Q5. Stop at the first number divisible by 7

Go through numbers 1 to 50. As soon as you find a number divisible by 7, print it and stop.

Think before coding:
Check each number → is i % 7 == 0?
If yes → print it and break
If no → keep going
show hint show solution
'''




'''
count = 1
while count <= 50:
    if(count%7==0):
        print(f"divisible by 7 is this number-> {count}")
        break
    else:
        print("finding")
        count = count+1
'''











'''
find first → break
Q1. First number divisible by 5

Go through numbers 1 to 50. Find the first number divisible by 5, print it and stop.

Think before coding:
Start → i = 1
Check → is i % 5 == 0 ?
If yes → print it and break
If no → keep going (i += 1)

'''




#i = 1


# count = 0
# while i <=50:
#     if (i%5==0):
#         print(f"{i} is on {[count]} position")
#         break
#     else:
#         print("finding")
#         i+=1
#         count+=1










'''
Q2. First number greater than 50 in a multiplication table

Start with n = 6. Keep multiplying by 6 (6, 12, 18...). Find the first result that goes above 50 and print it.

Think before coding:
Start → n = 6
Check → is n > 50 ?
If yes → print it and break
If no → multiply n by 6 again

'''



'''
n = 6

while True:
    if n > 50:
        print(f"first above 50: {n}")
        break
    else:
        print("finding...")
        n += 6
'''




'''
Q3. First number divisible by BOTH 2 and 3

Go through numbers 1 to 30. Find the first number divisible by both 2 and 3. Print it and stop.

Think before coding:
Start → i = 1
Check → is i % 2 == 0 AND i % 3 == 0 ?
If yes → print and break
If no → i += 1

'''





# i = 1

# while i<=30:
#     if(i%2==0 and i%3==0):
#         print(f"number->  {i}")
#         break
#     else:
#         print("finding")
#         i += 1
















'''
Q4. First number whose square exceeds 200

Go through numbers 1, 2, 3... Find the first number whose square (n²) is greater than 200. Print the number and its square.

Think before coding:
Start → i = 1
Check → is i * i > 200 ?
If yes → print i and i*i, then break
If no → i += 1

'''




# i = 1

# while i<200:
#     if(i*i>200):
#         print(f"number {i}")
#         break
#     else:
#         print("next")
#         i+=1





'''
Q5. Find the first number that is NOT divisible by 2

You have a list: nums = [2, 4, 6, 7, 8, 10]. Go through it and find the first number that is odd (not divisible by 2). Print it and stop.

Think before coding:
Start → index = 0
Check → is nums[index] % 2 != 0 ?
If yes → print and break
If no → index += 1

'''

'''
nums = [2, 4, 6, 7, 8, 10]
index = 0
while index < len(nums):
    if nums[index] % 2 != 0:
        print(f"first odd number: {nums[index]}")
        break
    else:
        index += 1
'''







'''
Q6. First number divisible by 4 but NOT by 8

Go through numbers 1 to 100. Find the first number divisible by 4 but NOT divisible by 8. Print it and stop.

Think before coding:
Start → i = 1
Check → is i % 4 == 0 AND i % 8 != 0 ?
If yes → print and break
If no → i += 1

'''








# i = 1

# while i < 100:
#     if(i % 4== 0 and i % 8 != 0):
#         print(i)
#         break
#     else:
#         ("finding")
#         i+=1


















'''
Q6. Print numbers 1–10, skip 5 and 8

Print all numbers from 1 to 10 but skip 5 and 8 using continue.

Think before coding:
For each number → is it 5 or 8?
If yes → skip (continue)
If no → print it

'''





# i = 0

# while i<10:
#     if(i==5 or i==8):
#         i+=1
#         continue
#     else:
#         print(i)
#         i+=1












'''

Q7. Add numbers until sum crosses 20

Start adding 1, 2, 3, 4 ... one by one. Stop as soon as the total crosses 20. Print how many numbers you added.

Think before coding:
Track two things → total (sum) and count (how many added)
Stop when → total exceeds 20
Each step → add next number, increase cou
'''

# a = [10,20,30,40,50]


# index = 0
# sum = 0

# while index<len(a):
#     sum += a[index]
#     index += 1

# print(sum)
'''
i = 1
total = 0

while total <= 20:
    total += i
    i += 1

print(f"numbers added: {i - 1}")
print(f"final sum: {total}")
'''


















'''
Q1. Add numbers until sum crosses 50

Start adding 1, 2, 3, 4... one by one. Stop as soon as total crosses 50. Print how many numbers you added and the final sum.

Think before coding:
Track → total (sum), i (current number)
Stop when → total > 50
Each step → total += i, then i += 1
After loop → print i-1 (count) and total

'''


# i = 1

# total = 0

# while total<50:
#     total+=i
#     i+=1

# print(f"all numbers added: {i-1}")
# print(f"sumof these numbers: {total}")

















'''

Q2. Add only even numbers until sum crosses 30

Start adding 2, 4, 6, 8... (even numbers only) one by one. Stop as soon as total crosses 30. Print how many even numbers you added.

Think before coding:
Track → total, i (start at 2, jump by 2)
Stop when → total > 30
Each step → total += i, then i += 2
After loop → print count of numbers added
'''





# i = 2

# total = 0

# while total<30:
#     total+=i
#     i+=2
# print(f"all numbers added: {i-1}")
# print(f"sumof these numbers: {total}")






'''
Q3. Keep multiplying until product crosses 1000

Start with product = 1. Keep multiplying by 2 each step (1, 2, 4, 8...). Stop when product crosses 1000. Print how many multiplications you did.

Think before coding:
Track → product, count
Stop when → product > 1000
Each step → product *= 2, count += 1
After loop → print count and product

'''




'''
product = 1

count = 0

while product<1000:
    product *= 2
    count += 1

print(f"total numbers: {count}")
print(f"total {product}")
'''











'''
Q4. Save money until you reach 500

You save money each week. Week 1 → save ₹10, Week 2 → save ₹20, Week 3 → save ₹30... (increases by 10 each week). How many weeks to save ₹500 or more?

Think before coding:
Track → savings (total), week (count), amount (10, 20, 30...)
Stop when → savings >= 500
Each step → savings += amount, amount += 10, week += 1
After loop → print week and savings

'''


# amount = 10

# week_count = 0

# savings_total = 0

# while savings_total<500:
#     savings_total+=amount
#     amount+=10
#     week_count+=1
# print(f"total weeks {week_count}")
# print(f"total savings {savings_total}")






# i = 1

# total = 0

# count = 0

# while total<20:
#     if(i % 3 == 0):
#         i+=1
#         continue
#     else:
#         total+=i
#         i+=1
#         count+=1

# print(f"numbers actually added: {count}")
# print(f"total_sum: {total}")




'''
Q6. Add numbers but stop if you hit a multiple of 7

Add numbers 1, 2, 3... to a total. But if the current number is a multiple of 7, stop immediately using break. Print the total collected before stopping and how many numbers were added.

Think before coding:
Track → total, count, i
Stop early when → i % 7 == 0 (break)
Otherwise → total += i, count += 1, i += 1
After loop → print total and count

'''




# i = 1

# total = 0

# count = 0


# while total<=7:
#     if(i%7==0):
#         break
#     else:
#         total+=i
#         i+=1
#         count+=1

# print(f"how mamy number added: {count}")
# print(f"how mamy number added: {i-1}")
# print(f"total sum: {total}")


















'''
Q7. Add numbers, skip multiples of 4, stop when total crosses 40

Add numbers 1, 2, 3... but skip any multiple of 4 using continue. Stop as soon as total crosses 40 using the while condition. Print total and count of numbers added.

Think before coding:
Track → total, count, i
Skip when → i % 4 == 0 (continue)
Stop when → total > 40 (while condition)
Each step → add to total, count += 1, i += 1

'''


'''
i = 1

total = 0

count = 0

while total<=40:
    if(i%4==0):
        i+=1
        continue
    else:
        total+=i
        i+=1
        count+=1

        
print(f"numbers added: {count}")
print(f"total: {total}")
'''



'''
Q3. Find first even number

Given a list nums = [1, 3, 7, 4, 9, 2], use a while loop with break to find and print the first even number.

'''



'''
nums = [1, 3, 7, 4, 9, 2]

count = 0

while count<=len(nums):
    if nums[count]%2==0:
        print(f"even number: {nums[count]}")
        count+=1
        break
    else:
        count+=1
    '''
    



'''
Q4. Password attempt limiter

Simulate a login system. The correct password is "python123". Give the user 3 attempts using a while loop. Break if they get it right. Print "Access granted" or 
"Access denied" accordingly.

'''


'''
i = input("enter password: ")
correct = "python123"
attempts = 1

while attempts<=3:
    if i==correct:
        print("Access granted")
        break
    else:
        if attempts == 3:
            print("Attempts Completed !!! Account Blocked")
            break
        else:
            print(f"Attempt {attempts} for password done.. Attempt left {3-attempts}")
            i = input("enter password again: ")
            attempts+=1
'''












'''
continue
Q5. Skip multiples of 3

Print numbers from 1 to 15 using a while loop, but skip any number that is a multiple of 3 using continue.
'''




# i = 1

# while i<15:
#     if i%3==0:
#         i+=1
#         continue
#     else:
#         print(i)
#         i+=1







'''
Q6. Print only odd numbers

Use a while loop to print only odd numbers from 1 to 20 using the continue statement.

'''

'''
i = 1

while i<20:
    if i%2==0:
        i+=1
        continue

    print(i)
    i+=1
'''






'''

Q7. Number guessing game

Write a number guessing game. The secret number is 42. Keep asking the user to guess using a while loop. Print 'Too low', 'Too high', 
or 'Correct!' and break on the right answer.

'''


'''
secret_number = 42

while True:
    i = int(input("enter number: "))  # ask inside loop every time
    if i == secret_number:
        print("Correct!")
        break
    elif i > secret_number:
        print("too high")
    elif i < secret_number:
        print("too low")
'''




'''
Q8. Collect valid inputs

Ask the user to enter positive numbers one by one. Use continue to skip negatives (print a warning), and break when 0 is entered.
At the end print the sum of valid inputs.

'''

'''
total = 0

while True:
    i = int(input("enter number: "))

    if i == 0:
        break
    elif i < 0:
        print("Warning: negative number skipped!")
        continue
    else:
        total += i

print(f"total of all valid numbers: {total}")
'''










# *****************************************************************************************************************************************
#******************************************************************************************************************************************
#******************************************************************************************************************************************
#******************************************************************************************************************************************
#******************************************************************************************************************************************
#******************************************************************************************************************************************



'''
for loop

'''




'''
list = [1,4,9,15,25,36,49,64,81,100]

for var in list:
    print(var)
'''




    
# list = [1,2,3,4,5,6]
# list_even = []
# list_odd = []
# for i in list:
#     if i%2==0:
#         list_even.append(i)
#     else:
#         list_odd.append(i)
    

# print(list_odd)
# print(list_even)












# t_shirt = ["Red","Yellow","Black"]
# sizes = ["M","L","XL"]

# #cartesion product
# #Brute Force : time complexity : o(n2)
# for t in t_shirt:
#     for s in sizes:
#         print(f"for T-Shirt with color {t}, size present is {s}")
      










'''
normal for
Q1. Print each item in a list

Given fruits = ["apple","banana","mango","grape"], print each fruit one by one using a for loop.

Think before coding:
Loop variable → fruit
Loop over → fruits list
Each step → print fruit

'''
'''
fruits = ["apple","banana","mango","grape"]

for i in fruits:
    print(i)
    '''



'''

Q2. Sum all numbers in a list

Given nums = [3, 7, 2, 9, 4], find the sum of all numbers using a for loop.

Think before coding:
Track → total = 0
Loop over → nums
Each step → total += num

'''


# nums = [3, 7, 2, 9, 4]


# total = 0

# for i in nums:
#     total += i

# print(f"total is equals {total}")





'''
Q3. Count how many times "a" appears in a string

Given word = "banana", count how many times the letter "a" appears using a for loop.

Think before coding:
Track → count = 0
Loop over → each letter in word
Each step → if letter == "a": count += 1

'''


'''
word = "banana"

count = 0

for letter in word:
    if (letter == "a"):
        count+=1

print(f"total count {count}")
'''



'''
range
Q4. Print numbers 1 to 10 using range

Print numbers from 1 to 10 using a for loop with range().

Think before coding:
range(start, stop) → stop is excluded
So range(1, 11) gives 1 to 10

'''


'''
for i in range(1,11):
    print(i)
'''







'''
Q5. Print multiplication table of 5

Print the multiplication table of 5 (5×1 to 5×10) using range().

Think before coding:
Loop i from 1 to 10
Each step → print 5 × i

'''


'''
for i in range(1,11):
    print(5*i)
   ''' 





'''
Q6. Print even numbers from 2 to 20 using range step

Print even numbers 2, 4, 6... 20 using range() with a step value.

Think before coding:
range(start, stop, step)
Start at 2, stop at 21, step by 2

'''


'''
for i in range(2,21,2):
    print(i)
'''



'''
Q7. Count down from 10 to 1 using range

Print numbers from 10 down to 1 using range() with a negative step.

Think before coding:
range(start, stop, step)
Start at 10, stop before 0, step by -1

'''


'''
for i in range(10,0,-1):
    print(i)
'''






'''

Q8. Check if a number exists in a list

Given nums = [3, 7, 2, 9, 4], check if 5 exists. Use for-else — print "found" if it does, "not found" if it doesn't.

Think before coding:
Loop over nums
If num == 5 → print "found" and break
else (no break happened) → print "not found"

'''
'''
nums = [3, 7, 2, 9, 4]

for target in nums:
    if target == 5:
        print(f" found {target} ")
        break
else:
    print("not found")
    '''




'''
Q9. Find first negative number in a list

Given nums = [4, 7, 2, -3, 9], find the first negative number using for-else. If no negative exists, print "all positive".

Think before coding:
Loop over nums
If num < 0 → print it and break
else → print "all positive"

'''


# nums = [4, 7, 2, -3, 9]

# for target in nums:
#     if target < 0 :
#         print(f" found negative {target} ")
#         break
# else:
#     print("all positive")




'''
for-else
Q10. Check if all numbers are even

Given nums = [2, 4, 6, 8], check if ALL numbers are even. Print "all even" or "not all even".

Think before coding:
Loop over nums
If any num is odd → print "not all even" and break
else → print "all even"

'''

'''
nums = [2, 4, 7, 8]

for i in nums:
    if i%2!=0:
        print("not all even")
        break
else:
    print("all even")
'''











'''

Q11. Skip even numbers using pass

Loop through 1 to 10. Use pass for even numbers (do nothing) and print odd numbers.

Think before coding:
Loop i from 1 to 10
If even → pass (do nothing)
If odd → print it
'''


'''
for i in range(1,10):
    if i%2==0:
        pass
    else:
        print(i)
'''     





'''
Q12. Build an empty structure using pass

Loop through a list categories = ["food","travel","tech"]. For "travel" do nothing (pass), for others print "processing: category".

Think before coding:
Loop over categories
If category == "travel" → pass
Else → print processing message

'''


'''
categories = ["food","travel","tech"]

for i in categories:
    if i == "travel":
        pass
    else:
        print(f"proceesing: {i}")
'''










'''
Q1. Find the largest number in a list

Given nums = [3, 7, 2, 9, 4, 1], find the largest number using a for loop. Do not use max().

Think before coding:
Track → largest = first item
Loop over → rest of list
Each step → if num > largest: update largest

'''


# nums = [3, 7, 2, 9, 4, 1]

# largest = nums[0]

# for i in nums:
#     if i > largest:
#         i+=largest
#     else:
#         print()


# nums = [3, 7, 2, 9, 4, 1]
# largest = nums[0]

# for i in nums:
#     if i > largest:
#         largest = i

# print(f"largest: {largest}")


# num = 1

# while num<=10:
#     print(num)
#     num+=1







'''
Q2. Reverse a string using for loop

Given word = "python", build the reversed string using a for loop. Do not use word[::-1].

Think before coding:
Track → result = ""
Loop over → each letter in word
Each step → add letter to FRONT of result

'''







# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************
# *****************************************************************************************************************************************


# Q1
# Easy
# Print 0 to 4 using for loop.
# 💡 Show Hint
# ✅ Show Solution


# for i in range(5):
#     print(i)


# Q2
# Easy
# Print 1 to 5 using while loop.
# 💡 Show Hint
# ✅ Show Solution

# i= 1

# while i <= 5:
#     print(i)
#     i+=1


# Q3
# Easy
# Even numbers 0 to 10.
# 💡 Show Hint
# ✅ Show Solution

# for i in range(0,11,2):
#     print(i)

# i = 0
# while i <= 10:
#     print(i)
#     i += 2


# Q4
# Easy
# Loop ['a','b','c','d'] and print each.
# 💡 Show Hint
# ✅ Show Solution


# for l in ['a','b','c','d']:
#     print(l)




# Q5
# Easy
# What does 'pass' do?
# 💡 Show Hint
# ✅ Show Solution

# igonres the current statement and does nothing. used for any placeholder furture code.




# Q6
# Medium
# break when finding 5 in [1,3,7,5,9,2].
# 💡 Show Hint
# ✅ Show Solution

# for i in [1,3,7,5,9,2]:
#     if i == 5:
#         print("found breaking point", i)
#         break
#     else:
#         print("finding")
        

        
# li = [1,3,7,5,9,2]

# i = 0
# while i < len(li):
#     if li[i] == 5:
#         print("found breaking point", li[i])
#         break
#     else:
#         print("finding")
#     i += 1



# Q7
# Medium
# continue to skip multiples of 3 printing 1–10.
# 💡 Show Hint
# ✅ Show Solution

# for i in range(1,11):
#     if i%3==0:
#         continue
#     print(i)

# st = 1

# while st <= 10:
#     if st % 3 == 0:
#         st += 1
#         continue
#     print(st)
#     st += 1

# Q8
# Medium
# Multiplication table for 5.
# 💡 Show Hint
# ✅ Show Solution

# for i in range(1,11):
#     print(i*5)

# st = 1
# while st <= 10:
#     print(st*5)
#     st+=1


# Q9
# Medium
# Predict:

# for i in range(5,0,-1):
#     print(i)
# 💡 Show Hint
# ✅ Show Solution

# 5
# 4
# 3
# 2
# 1






# Q10
# Medium
# While loop with break: stop when x hits 0.
# 💡 Show Hint
# ✅ Show Solution


# x=5
# while True:
#     if x==0: break
#     print(x)
#     x-=1






# Q11
# Hard
# enumerate() on ['apple','banana','cherry'].
# 💡 Show Hint
# ✅ Show Solution

# for i,f in enumerate(['apple','banana','cherry']):
#     print(i,f)




# Q12
# Hard
# Even numbers from [1..8] using list comprehension.
# 💡 Show Hint
# ✅ Show Solution


# not understanding




# Q13
# Hard
# Predict:

# for i in range(3):
#     pass
# else:
#     print('done')
# 💡 Show Hint
# ✅ Show Solution


# output: done



# Q14
# Hard
# Count vowels in 'Hello World'.
# 💡 Show Hint
# ✅ Show Solution

# for i in ['Hello World']:
#     print(f"a is {i.count('a')} time ")
#     print(f"e is {i.count('e')} time ")
#     print(f"i is {i.count('i')} time ")
#     print(f"o is {i.count('o')} time ")
#     print(f"u is {i.count('u')} time ")
    




# Q15
# Hard
# Print star pattern:
# *
# **
# ***
# ****
# *****


# for i in range(1,6):
#       print(i*"*")

