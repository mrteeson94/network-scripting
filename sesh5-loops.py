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
for i in range(100, 0, -1):
    print(i)
