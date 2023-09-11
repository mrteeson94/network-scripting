#   practice
# **EX1: WHILE LOOP**
# a.Print 10 to 1
# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# b.Print 1 up to 16
# i = 1
# while i < 16:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 16")

# **EX2: FOR LOOP**
# a.Print numbers in a given range 1 - 10 and their squares
# print("Number Square")
# print("...........")
# for i in range(1, 11):
#     print(i, '\t', i*i)

# b.print even numbers in between 1 and 100
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)
# input_one = int(input("What is the starting number for the table: "))
# input_two = int(input("What is the ending number for the table: "))
# print("Number Square")
# print("...........")
# for i in range(input_one, input_two+1):
#     print(i, '\t', i*i)

# c. Print 100 down to 1
# for i in range(100, 0, -1):
#     print(i)

# d. get 5 inputs, print total of the 5 inputs
# total = 0
# for i in range(1, 5):
#     current_input = int(input(f"Insert a number that will be summed {i}.:"))
#     total += current_input
#     print(f"your input: {current_input},current total: {total}")
# print(total)

# **EX3: test score, get user input and check if num exist in range 1 - 100**
# user_input = int(input("Insert your test mark:"))
# status = False
# for i in range(0, 101):
#     if i == user_input:
#         status = True
# if status:
#     print(f"Your result:{user_input}")
# else:
#     print("Invalid result number, please provide it as a number(0 - 100)")

# **EX4: print a staircase pattern with '*' with a base of 8 **
# MAX = 8
# MIN = 1
# for i in range(MIN, MAX):
#     print(i*"*")

# **EX5:
# a) display even numbers 100 to 10 **
# for i in range(100, 9, -2):
#     print(i)
# b) display the triangle pattern using nested for loops
# FOR LOOP 1 - only used to nest the 2nd loop
# FOR LOOP 2 -IF-ELSE to check
# end="" removes newline, we used print() in 1st loop to create new row, otherwise all print will remain in 1 row
MAX = 5
for i in range(MAX):
    for j in range(i):
        print('*', end="")
    print(' ')
for i in range(MAX, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')
